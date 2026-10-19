# SQL — People Analytics RH

Consultas PostgreSQL para perfil do quadro, movimentações, remuneração, qualidade dos dados, window functions e views.

- `scripts/00_diagnostico_banco.sql`: inventário de tabelas, colunas e constraints.
- `consultas/01_perfil_funcionarios.sql`: quadro na data de referência.
- `consultas/02_quadro_por_area.sql`: distribuição por área, cargo e nível.
- `consultas/03_admissoes_desligamentos.sql`: movimentação mensal e saldo.
- `consultas/04_analise_remuneracao.sql`: composição do custo mensal.
- `consultas/05_qualidade_dados.sql`: verificações básicas de qualidade.
- `consultas/06_window_functions.sql`: ranking por área.
- `consultas/07_views_analiticas.sql`: views reutilizáveis.

Confira os nomes e tipos reais das colunas antes de executar. As consultas são scripts iniciais e devem ser testadas no banco local.
