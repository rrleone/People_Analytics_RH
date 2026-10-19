# People Analytics RH

Projeto de análise de dados de Recursos Humanos desenvolvido com Python, PostgreSQL, SQL e Power BI, com foco em qualidade dos dados, análise do quadro de pessoal, movimentações e custos de remuneração.

## Objetivo

Transformar dados de RH em informações para apoiar decisões de gestão de pessoas, permitindo analisar o perfil dos funcionários, a evolução do quadro, as movimentações e a composição dos custos de pessoal.

## Dashboard Power BI

Arquivo: `05_PowerBI/People_analytics.pbix`

O dashboard está organizado em quatro páginas:

1. **Visão Executiva** — indicadores gerais e evolução do quadro de pessoal.
2. **Perfil RH** — distribuição dos funcionários e características do quadro.
3. **Remuneração** — custos de pessoal, componentes remuneratórios e diferenças entre áreas.
4. **Turnover** — admissões, desligamentos e análises de movimentação.

As imagens de apresentação estão disponíveis em `07_Portfolio/`.

## Pipeline de dados

1. Organização dos dados originais e tratados em `01_Dados/`.
2. Validação de dados com Python em `02_Python/validar_base_people_analytics.py`.
3. Carga dos dados tratados no PostgreSQL.
4. Consultas analíticas e verificações SQL em `03_SQL/`.
5. Documentação da estrutura de dados em `04_Modelagem/`.
6. Construção do dashboard em Power BI.

## Tecnologias

- Python
- PostgreSQL
- SQL
- Power BI
- DAX
- CSV

## Validação dos dados

O script `02_Python/validar_base_people_analytics.py` verifica contagens, duplicidades, datas, eventos de RH, remuneração, dimensões e consistência do quadro mensal.

O relatório de validação é gerado em `01_Dados/03_Validacao/`, conforme a configuração do script.

## Banco de dados PostgreSQL

A base utilizada é `people_analytics_rh`, no schema `public`.

A carga das oito tabelas restantes foi concluída por meio do script `02_Python/carregar_csvs_postgresql_seguro_v2.py`, preservando a tabela `funcionarios`.

Contagens verificadas após a carga:

| Tabela | Registros |
|---|---:|
| `funcionarios` | 600 |
| `dim_area` | 8 |
| `dim_cargo` | 31 |
| `dim_localidade` | 10 |
| `dim_nivel` | 6 |
| `dim_calendario` | 1.369 |
| `eventos_rh` | 690 |
| `historico_quadro_mensal` | 45 |
| `historico_remuneracao` | 12.466 |

A consulta de perfil na data de referência de 30/09/2026 retornou 600 funcionários cadastrados, 510 ativos e 90 desligados.

Essas verificações confirmam as contagens e os indicadores de perfil consultados; não representam, por si só, uma auditoria integral de todas as regras de negócio.

## Estrutura do projeto

- `01_Dados/` — dados originais, dados tratados e relatórios de validação.
- `02_Python/` — scripts de validação e carga.
- `03_SQL/` — consultas, scripts de diagnóstico e views analíticas.
- `04_Modelagem/` — documentação da modelagem de dados.
- `05_PowerBI/` — arquivo do dashboard.
- `06_Documentacao/` — documentação técnica e metodológica.
- `07_Portfolio/` — imagens de apresentação do projeto.

## Status do projeto

- Dashboard Power BI desenvolvido.
- Oito tabelas restantes carregadas no PostgreSQL.
- Nove tabelas verificadas por contagem de registros.
- Consulta de perfil executada e resultados conferidos.
- Consultas SQL adicionais e modelagem relacional ainda sujeitas à validação específica.
- README preparado para revisão final antes da publicação.

## Próximos passos

1. Revisar os arquivos que serão publicados.
2. Excluir credenciais, arquivos temporários e dados pessoais ou confidenciais.
3. Publicar o repositório no GitHub.
4. Preparar a apresentação do projeto no LinkedIn.
