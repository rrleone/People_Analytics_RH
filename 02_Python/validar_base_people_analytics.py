#!/usr/bin/env python3
"""Validação somente de leitura da base People Analytics RH.
Uso na raiz do projeto:
python3 02_Python/validar_base_people_analytics.py --pasta 01_Dados/02_Tratados
"""
import argparse, csv, sys
from pathlib import Path
from datetime import date
from collections import Counter

REF = date(2026, 9, 30)

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def dt(value):
    value = (value or "").strip()
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return "INVALIDA"

def dup(values):
    return len(values) - len(set(values))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", default=".", help="Pasta com os nove CSVs")
    args = ap.parse_args()
    folder = Path(args.pasta).expanduser().resolve()
    names = {
        "func": "funcionarios.csv", "eventos": "eventos_rh.csv",
        "rem": "historico_remuneracao.csv", "quadro": "historico_quadro_mensal.csv",
        "cal": "dim_calendario.csv", "area": "dim_area.csv",
        "cargo": "dim_cargo.csv", "local": "dim_localidade.csv", "nivel": "dim_nivel.csv"
    }
    missing = [v for v in names.values() if not (folder / v).is_file()]
    if missing:
        sys.exit("Arquivos ausentes: " + ", ".join(missing))
    d = {k: read_csv(folder / v) for k, v in names.items()}
    f, ev, rem, q, cal = d["func"], d["eventos"], d["rem"], d["quadro"], d["cal"]
    results = []
    def check(name, n):
        results.append((name, int(n)))
    ids = [r["id_funcionario"].strip() for r in f]
    ids_set = set(ids)
    by_id = {r["id_funcionario"].strip(): r for r in f}
    admission = {i: dt(r["data_admissao"]) for i, r in by_id.items()}
    dismissal = {i: dt(r["data_demissao"]) for i, r in by_id.items()}

    check("Funcionários (esperado 600)", abs(len(f)-600))
    check("IDs de funcionário duplicados", dup(ids))
    check("Nulos fora de data_demissao", sum(not (v or "").strip() for r in f for k,v in r.items() if k!="data_demissao"))
    check("Admissões ausentes/ inválidas", sum(admission[i] is None or admission[i]=="INVALIDA" for i in ids))
    check("Desligamentos com data inválida", sum(dismissal[i]=="INVALIDA" for i in ids))
    check("Desligamentos anteriores à admissão", sum(isinstance(admission[i],date) and isinstance(dismissal[i],date) and dismissal[i]<admission[i] for i in ids))
    check("Desligamentos após 30/09/2026", sum(isinstance(dismissal[i],date) and dismissal[i]>REF for i in ids))
    check("Funcionários ativos (esperado 510)", abs(sum(dismissal[i] is None for i in ids)-510))
    check("Desligados (esperado 90)", abs(sum(isinstance(dismissal[i],date) for i in ids)-90))

    event_ids = [r["id_evento"].strip() for r in ev]
    check("IDs de evento duplicados", dup(event_ids))
    check("Eventos com funcionário inexistente", sum(r["id_funcionario"].strip() not in ids_set for r in ev))
    check("Admissões sem evento", sum(sum(1 for e in ev if e["id_funcionario"].strip()==i and e["tipo_evento"].strip()=="Admissão") != 1 for i in ids))
    check("Desligamentos sem evento", sum(isinstance(dismissal[i],date) != any(e["id_funcionario"].strip()==i and e["tipo_evento"].strip()=="Desligamento" for e in ev) for i in ids))

    rem_ids = [r["id_registro_remuneracao"].strip() for r in rem]
    check("IDs de remuneração duplicados", dup(rem_ids))
    pairs = [(r["id_funcionario"].strip(), r["data_referencia"].strip()) for r in rem]
    check("Duplicidades funcionário + mês remuneração", dup(pairs))
    check("Remuneração sem funcionário correspondente", sum(r["id_funcionario"].strip() not in ids_set for r in rem))

    count_by_date = Counter()
    latest = {}
    before_hire = after_exit = bad_dates = negative = 0
    money_cols = ["salario_base_mensal","encargos_mensais","beneficios_mensais","vale_transporte_mensal","vale_refeicao_mensal","provisao_ferias_mensal","horas_extras_mensais","adicionais_mensais"]
    for r in rem:
        i = r["id_funcionario"].strip()
        day = dt(r["data_referencia"])
        if not isinstance(day,date):
            bad_dates += 1
            continue
        if isinstance(admission.get(i),date) and day < admission[i]: before_hire += 1
        if isinstance(dismissal.get(i),date) and day >= dismissal[i]: after_exit += 1
        count_by_date[day] += 1
        if i not in latest or day > latest[i][0]: latest[i] = (day,r)
        for c in money_cols:
            try:
                if float(r.get(c,"0") or 0) < 0: negative += 1
            except ValueError:
                negative += 1
    check("Datas de remuneração ausentes/inválidas", bad_dates)
    check("Remuneração antes da admissão", before_hire)
    check("Remuneração no mês da demissão ou depois", after_exit)
    check("Valores negativos em remuneração", negative)

    area_ids = {r["id_area"].strip() for r in d["area"]}
    area_map = {r["id_area"].strip():r["area"].strip() for r in d["area"]}
    check("IDs de área inválidos", sum(r["id_area"].strip() not in area_ids for r in f))
    check("Nomes de área divergentes", sum(area_map.get(r["id_area"].strip()) != r["area"].strip() for r in f))
    cargo_keys = {(r["cargo"].strip(),r["nivel"].strip(),r["id_area"].strip()) for r in d["cargo"]}
    check("Cargo/nível/área sem dimensão", sum((r["cargo"].strip(),r["nivel"].strip(),r["id_area"].strip()) not in cargo_keys for r in f))
    loc_keys = {(r["cidade"].strip(),r["uf"].strip(),r["regiao"].strip()) for r in d["local"]}
    check("Localidade sem dimensão", sum((r["cidade"].strip(),r["uf"].strip(),r["regiao"].strip()) not in loc_keys for r in f))
    levels = {r["nivel"].strip() for r in d["nivel"]}
    check("Nível sem dimensão", sum(r["nivel"].strip() not in levels for r in f))

    qmap = {}
    for r in q:
        day = dt(r["data_referencia"])
        try: n = int(r["funcionarios_ativos_fim_mes"])
        except ValueError: n = -999999
        qmap[day] = n
    qdiff = rdiff = 0
    for day, given in qmap.items():
        if not isinstance(day,date):
            qdiff += 1; continue
        calculated = sum(isinstance(admission[i],date) and admission[i] <= day and not (isinstance(dismissal[i],date) and dismissal[i] <= day) for i in ids)
        if calculated != given: qdiff += 1
        if count_by_date[day] != given: rdiff += 1
    check("Meses com quadro divergente", qdiff)
    check("Meses com remuneração diferente do quadro", rdiff)

    pairs_salary = [
        ("salario_base_mensal","salario_base_mensal_atual"),
        ("encargos_mensais","encargos_mensais_atual"),
        ("beneficios_mensais","beneficios_mensais_atual"),
        ("vale_transporte_mensal","vale_transporte_mensal_atual"),
        ("vale_refeicao_mensal","vale_refeicao_mensal_atual"),
        ("provisao_ferias_mensal","provisao_ferias_mensal_atual"),
        ("horas_extras_mensais","horas_extras_mensais_atual"),
        ("adicionais_mensais","adicionais_mensais_atual")]
    salary_diff = 0
    for i, (_, r) in latest.items():
        for hist, cur in pairs_salary:
            try:
                if abs(float(r.get(hist,"0") or 0)-float(by_id[i].get(cur,"0") or 0)) > .01: salary_diff += 1
            except (ValueError, KeyError): salary_diff += 1
    check("Últimos componentes de remuneração divergentes da base", salary_diff)
    cal_dates = [r["data"].strip() for r in cal]
    check("Datas duplicadas no calendário", dup(cal_dates))
    check("Datas vazias no calendário", sum(not x for x in cal_dates))
    check("Meses duplicados no quadro mensal", dup([r["data_referencia"].strip() for r in q]))

    print(f"Pasta auditada: {folder}")
    print(f"Funcionários={len(f)} | Eventos={len(ev)} | Remunerações={len(rem)} | Meses={len(q)} | Datas calendário={len(cal)}")
    print("\nRESULTADOS")
    for name, n in results:
        print(f"[{'OK' if n == 0 else 'VERIFICAR'}] {name}: {n}")
    fails = sum(n != 0 for _,n in results)
    report_dir = folder.parent / "03_Validacao"
    if not report_dir.exists(): report_dir = folder
    report_dir.mkdir(parents=True, exist_ok=True)
    report = report_dir / "relatorio_validacao_gerado.csv"
    with report.open("w",encoding="utf-8-sig",newline="") as out:
        w = csv.writer(out)
        w.writerow(["teste","quantidade_de_ocorrencias"])
        w.writerows(results)
    print(f"\nRelatório salvo em: {report}")
    print(f"Testes com ocorrências: {fails}")
    if fails: sys.exit(1)

if __name__ == "__main__":
    main()
