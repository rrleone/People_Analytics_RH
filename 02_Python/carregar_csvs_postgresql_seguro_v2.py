#!/usr/bin/env python3
"""Carga segura das oito tabelas restantes; preserva public.funcionarios."""
import argparse, csv, os, sys
from getpass import getpass
from pathlib import Path
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

try:
    import psycopg2
    from psycopg2 import sql
    from psycopg2.extras import execute_batch
except ImportError:
    sys.exit("Dependência ausente: python3 -m pip install psycopg2-binary")

TABLES = [
    ("dim_area", "dim_area.csv"),
    ("dim_cargo", "dim_cargo.csv"),
    ("dim_localidade", "dim_localidade.csv"),
    ("dim_nivel", "dim_nivel.csv"),
    ("dim_calendario", "dim_calendario.csv"),
    ("eventos_rh", "eventos_rh.csv"),
    ("historico_quadro_mensal", "historico_quadro_mensal.csv"),
    ("historico_remuneracao", "historico_remuneracao.csv"),
]
DATE_NAMES = {"data", "data_nascimento", "data_admissao", "data_demissao", "data_evento", "data_referencia"}
INT_NAMES = {"id_funcionario", "id_area", "id_evento", "id_registro_remuneracao", "ordem_nivel", "ano", "mes_numero", "dia", "dia_semana"}
MONEY_NAMES = {
    "salario_base_mensal", "encargos_mensais", "beneficios_mensais",
    "vale_transporte_mensal", "vale_refeicao_mensal", "provisao_ferias_mensal",
    "horas_extras_mensais", "adicionais_mensais", "salario_base_mensal_atual",
    "encargos_mensais_atual", "beneficios_mensais_atual",
    "vale_transporte_mensal_atual", "vale_refeicao_mensal_atual",
    "provisao_ferias_mensal_atual", "horas_extras_mensais_atual", "adicionais_mensais_atual",
}
BOOL_NAMES = {"fim_de_semana", "is_weekend"}

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"CSV sem cabeçalho: {path}")
        headers = [h.strip() for h in reader.fieldnames]
        if len(headers) != len(set(headers)):
            raise ValueError(f"Cabeçalhos duplicados: {path}")
        rows = [
            {(k or "").strip(): (v.strip() if isinstance(v, str) else v)
             for k, v in row.items() if k is not None}
            for row in reader
        ]
        return headers, rows

def pg_type(column):
    n = column.lower()
    if n in DATE_NAMES or n.startswith("data_"): return "DATE"
    if n in BOOL_NAMES: return "BOOLEAN"
    if n in INT_NAMES or n.startswith("quantidade") or n.startswith("funcionarios_ativos"): return "INTEGER"
    if n in MONEY_NAMES or n.startswith("valor_") or n.startswith("salario") or n.startswith("encargos"): return "NUMERIC(14,2)"
    return "TEXT"

def parse_value(column, value):
    if value is None or value == "": return None
    n = column.lower()
    if n in DATE_NAMES or n.startswith("data_"):
        try: return date.fromisoformat(value[:10])
        except ValueError:
            try: return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
            except ValueError as e: raise ValueError(f"Data inválida em {column}: {value!r}") from e
    if n in BOOL_NAMES:
        if value.lower() in {"true", "t", "1", "sim", "yes"}: return True
        if value.lower() in {"false", "f", "0", "não", "nao", "no"}: return False
        raise ValueError(f"Booleano inválido em {column}: {value!r}")
    if n in INT_NAMES or n.startswith("quantidade") or n.startswith("funcionarios_ativos"):
        try: return int(value)
        except ValueError as e: raise ValueError(f"Inteiro inválido em {column}: {value!r}") from e
    if n in MONEY_NAMES or n.startswith("valor_") or n.startswith("salario") or n.startswith("encargos"):
        try: return Decimal(value.replace(",", "."))
        except InvalidOperation as e: raise ValueError(f"Número inválido em {column}: {value!r}") from e
    return value

def connection_config():
    dsn = os.getenv("DATABASE_URL")
    if dsn: return ("dsn", dsn)
    password = os.getenv("PGPASSWORD") or getpass("Senha do PostgreSQL (não será exibida): ")
    return ("params", {
        "host": os.getenv("PGHOST", "localhost"),
        "port": os.getenv("PGPORT", "5432"),
        "dbname": os.getenv("PGDATABASE", "people_analytics_rh"),
        "user": os.getenv("PGUSER", "postgres"),
        "password": password,
    })

def main():
    ap = argparse.ArgumentParser(description="Carga segura de oito tabelas; não altera public.funcionarios.")
    ap.add_argument("--pasta", default="01_Dados/02_Tratados")
    ap.add_argument("--schema", default="public")
    args = ap.parse_args()
    folder = Path(args.pasta).expanduser().resolve()
    datasets = []
    for table, filename in TABLES:
        path = folder / filename
        if not path.is_file(): sys.exit(f"Arquivo ausente: {path}")
        try: headers, rows = read_csv(path)
        except (OSError, ValueError) as e: sys.exit(str(e))
        datasets.append((table, headers, rows))

    try:
        mode, config = connection_config()
        connect = psycopg2.connect(config) if mode == "dsn" else psycopg2.connect(**config)
        with connect as conn:
            with conn.cursor() as cur:
                # Checa tudo antes de criar qualquer tabela.
                existing = []
                for table, _, _ in datasets:
                    cur.execute(
                        """SELECT EXISTS (
                            SELECT 1 FROM information_schema.tables
                            WHERE table_schema = %s AND table_name = %s
                        )""", (args.schema, table)
                    )
                    if cur.fetchone()[0]: existing.append(table)
                if existing:
                    raise RuntimeError(
                        f"Carga cancelada: já existem tabelas em {args.schema}: "
                        f"{', '.join(existing)}. Nenhuma tabela foi alterada."
                    )

                cur.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(args.schema)))
                for table, headers, rows in datasets:
                    definitions = sql.SQL(", ").join(
                        sql.SQL("{} {}").format(sql.Identifier(h), sql.SQL(pg_type(h)))
                        for h in headers
                    )
                    cur.execute(sql.SQL("CREATE TABLE {}.{} ({})").format(
                        sql.Identifier(args.schema), sql.Identifier(table), definitions
                    ))
                    if rows:
                        columns = sql.SQL(", ").join(sql.Identifier(h) for h in headers)
                        values = sql.SQL(", ").join(sql.Placeholder() for _ in headers)
                        query = sql.SQL("INSERT INTO {}.{} ({}) VALUES ({})").format(
                            sql.Identifier(args.schema), sql.Identifier(table), columns, values
                        ).as_string(conn)
                        payload = [[parse_value(h, row.get(h)) for h in headers] for row in rows]
                        execute_batch(cur, query, payload, page_size=500)
                    print(f"{table}: {len(rows)} registros carregados ({len(headers)} colunas)")
        print("\nCarga concluída. public.funcionarios foi preservada.")
    except Exception as e:
        sys.exit(f"\nCarga não concluída: {e}")

if __name__ == "__main__":
    main()
