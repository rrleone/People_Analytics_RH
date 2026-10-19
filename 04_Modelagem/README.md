# Modelagem de Dados — People Analytics RH

## Entidades
- `funcionarios`: cadastro de funcionários.
- `eventos_rh`: eventos de admissão e desligamento.
- `historico_quadro_mensal`: quadro ao fim do mês.
- `historico_remuneracao`: componentes remuneratórios por funcionário e referência.
- `dim_calendario`: calendário diário.
- `dim_area`, `dim_cargo`, `dim_localidade`, `dim_nivel`: dimensões de classificação.

## Granularidade esperada
- Funcionários: uma linha por funcionário (600 esperados).
- Eventos: uma linha por evento.
- Histórico de remuneração: uma linha por funcionário e referência.
- Histórico de quadro: uma linha por mês.
- Calendário: uma linha por data.

Documentar PK/FK e cardinalidades após validar o modelo real no Power BI e a integridade dos dados no PostgreSQL. Não presumir constraints antes da validação.
