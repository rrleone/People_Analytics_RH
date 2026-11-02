 <div align="center">

# PEOPLE ANALYTICS RH

### Human Resources Analytics · Workforce Intelligence · Turnover

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

**Análise de indicadores de Recursos Humanos para apoiar decisões de gestão de pessoas.**

</div>

---

## Visão geral do projeto

O **People Analytics RH** é um projeto de análise de dados desenvolvido para praticar um fluxo de trabalho de ponta a ponta em Análise de Dados e Business Intelligence aplicado ao contexto de Recursos Humanos.

O projeto reúne preparação e validação de dados com Python, armazenamento e consultas analíticas em PostgreSQL, exploração com SQL, modelagem e visualização de indicadores em dashboards desenvolvidos no Power BI.

> **Natureza do projeto:** laboratório educacional com dados fictícios e indicadores simulados. Os resultados não representam uma empresa real.

## Dashboards

### 01 · Visão Executiva

Apresentação consolidada dos principais indicadores do cenário simulado de Recursos Humanos.

![Visão Executiva](<07_Portfolio/01 - VISÃO EXECUTIVA.png>)

### 02 · Perfil RH

Exploração do perfil dos colaboradores, distribuição organizacional e tempo de empresa.

![Perfil RH](<07_Portfolio/02 - PERFIL RH.png>)

### 03 · Remuneração

Análise dos custos de pessoal, da composição remuneratória e dos indicadores relacionados à remuneração.

![Remuneração](<07_Portfolio/03 - REMUNERAÇÃO.png>)

### 04 · Turnover

Análise das movimentações simuladas de pessoal, incluindo admissões, desligamentos e indicadores de rotatividade.

![Turnover](<07_Portfolio/04 - TURNOVER.png>)

## Problema de negócio e objetivos

Em um cenário fictício de Recursos Humanos, a gestão precisa acompanhar a composição do quadro de funcionários, o perfil dos colaboradores, os custos de remuneração e as movimentações de pessoal.

O projeto simula o desenvolvimento de uma solução analítica para organizar essas informações, construir indicadores e apresentar resultados que apoiem a interpretação de cenários de gestão de pessoas.

**Objetivos:**

- Acompanhar a composição e evolução do quadro de funcionários.
- Analisar o perfil dos colaboradores e sua distribuição organizacional.
- Explorar custos e componentes de remuneração.
- Investigar admissões e desligamentos.
- Construir indicadores e dashboards para análise de RH.
- Demonstrar um fluxo de trabalho de ponta a ponta em Data Analytics e BI.

## Dados utilizados

O projeto utiliza uma base sintética desenvolvida para fins educacionais.

A base reúne informações relacionadas ao cadastro de funcionários, eventos de RH, histórico mensal do quadro de funcionários, remuneração e dimensões organizacionais.

| Tabela | Finalidade |
|---|---|
| `funcionarios` | Cadastro e características dos colaboradores fictícios |
| `eventos_rh` | Eventos simulados de admissão e desligamento |
| `historico_quadro_mensal` | Histórico mensal do quadro de funcionários |
| `historico_remuneracao` | Histórico mensal dos componentes remuneratórios |
| `dim_calendario` | Referência temporal para as análises |
| `dim_area` | Classificação das áreas organizacionais |
| `dim_cargo` | Classificação dos cargos |
| `dim_localidade` | Classificação das localidades |
| `dim_nivel` | Classificação dos níveis hierárquicos |

Os dados são utilizados exclusivamente para desenvolver e demonstrar procedimentos técnicos. Os indicadores devem ser interpretados dentro das regras e dos limites do cenário simulado.

## Metodologia analítica

O fluxo de trabalho contempla as seguintes etapas:

| Etapa | Processo | Objetivo |
|---|---|---|
| 01 | Data Profiling | Entendimento da estrutura, tipos e características dos dados |
| 02 | Data Quality | Verificação de valores ausentes, duplicidades, consistência e integridade |
| 03 | Data Preparation | Organização e preparação dos arquivos |
| 04 | Data Loading | Carga das tabelas no PostgreSQL |
| 05 | SQL Exploration | Exploração das entidades e estruturas de dados |
| 06 | Analytical Queries | Consultas sobre quadro, movimentações, remuneração e qualidade |
| 07 | Data Modeling | Organização das tabelas, dimensões e relacionamentos |
| 08 | Power BI Data Modeling | Configuração do modelo analítico, calendário e medidas DAX |
| 09 | Dashboard & KPIs | Construção das páginas executivas e analíticas |
| 10 | Business Insights | Interpretação dos resultados do cenário simulado |
| 11 | AI-Assisted Analysis | Utilização de IA como apoio, com revisão e validação humana |
| 12 | Documentation & Portfolio | Documentação técnica e organização dos materiais |

**Fluxo:** Dados → Qualidade → Análises → Modelagem → Indicadores → Dashboards → Insights.

## Indicadores e validações

Na consulta de perfil executada no PostgreSQL, foram registrados os seguintes resultados para a data de referência de **30/09/2026**:

| Indicador | Resultado registrado |
|---|---:|
| Funcionários cadastrados | 600 |
| Funcionários ativos | 510 |
| Funcionários desligados | 90 |

A classificação considera a data de admissão e a situação do desligamento na data de referência.

Esses valores correspondem à base sintética utilizada durante o desenvolvimento e não representam estatísticas de uma empresa real.

A validação técnica também contempla verificações de integridade, consistência e relacionamento entre as tabelas.

## Principais perspectivas analisadas

- **Workforce:** composição e evolução do quadro de funcionários.
- **Perfil organizacional:** distribuição entre áreas, cargos, níveis e localidades.
- **Remuneração:** custos de pessoal e componentes remuneratórios.
- **Movimentações:** admissões e desligamentos ao longo do tempo.
- **Turnover:** análise das movimentações e indicadores de rotatividade.
- **Tempo de empresa:** perfil de permanência dos colaboradores.

As análises devem ser interpretadas considerando os dados, as regras de negócio e os filtros aplicados. Por se tratar de um cenário sintético, os resultados não representam conclusões sobre uma organização real.

## Tecnologias e ferramentas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Automação, preparação e validação dos dados |
| PostgreSQL | Armazenamento e consulta das tabelas |
| SQL | Exploração, agregações, análises temporais e funções de janela |
| Power BI | Modelagem analítica e dashboards |
| DAX | Medidas e indicadores analíticos |
| Git / GitHub | Versionamento e documentação do projeto |
| Inteligência Artificial | Apoio ao desenvolvimento, depuração e documentação, com validação humana |

## Estrutura do repositório

```text
People_Analytics_RH/
├── 01_Dados/
│   ├── 01_Originais/
│   ├── 02_Tratados/
│   └── 03_Validacao/
├── 02_Python/
│   ├── carregar_csvs_postgresql_seguro_v2.py
│   └── validar_base_people_analytics.py
├── 03_SQL/
│   ├── scripts/
│   │   └── 00_diagnostico_banco.sql
│   ├── consultas/
│   │   ├── 01_perfil_funcionarios.sql
│   │   ├── 02_quadro_por_area.sql
│   │   ├── 03_admissoes_desligamentos.sql
│   │   ├── 04_analise_remuneracao.sql
│   │   ├── 05_qualidade_dados.sql
│   │   ├── 06_window_functions.sql
│   │   └── 07_views_analiticas.sql
│   └── README.md
├── 04_Modelagem/
│   └── README.md
├── 05_PowerBI/
│   └── People_analytics.pbix
├── 06_Documentacao/
│   ├── Guia_Comandos_People_Analytics_RH.pdf
│   └── Relatorio_Processo_People_Analytics_RH.pdf
├── 07_Portfolio/
│   ├── 01 - VISÃO EXECUTIVA.png
│   ├── 02 - PERFIL RH.png
│   ├── 03 - REMUNERAÇÃO.png
│   └── 04 - TURNOVER.png
├── .gitignore
└── README.md
```

A inclusão de arquivos de dados no repositório deve considerar a utilidade para reprodução, a consistência entre versões e a confirmação de que contêm somente dados sintéticos.

## Como reproduzir o projeto

Para reproduzir o laboratório em outro ambiente:

1. Instale e configure Python e as dependências necessárias.
2. Instale o PostgreSQL e crie o banco `people_analytics_rh`.
3. Disponibilize os arquivos sintéticos necessários no ambiente local.
4. Configure os parâmetros de conexão sem inserir senhas ou credenciais no código.
5. Execute `02_Python/carregar_csvs_postgresql_seguro_v2.py`, respeitando as verificações de segurança do script.
6. Consulte os arquivos SQL de `03_SQL/consultas/`.
7. Abra `05_PowerBI/People_analytics.pbix`.
8. Configure a conexão ao banco e atualize os dados.
9. Confira os indicadores apresentados e compare-os com as consultas de validação.

Os resultados podem variar conforme a versão dos arquivos, as regras de transformação e a configuração do ambiente.

> **Segurança:** não publique credenciais, senhas, arquivos `.env` ou informações confidenciais.

## Uso profissional de Inteligência Artificial

A IA foi utilizada como apoio ao desenvolvimento de scripts, consultas SQL, medidas, depuração e documentação.

O uso profissional da ferramenta é organizado em quatro dimensões:

- **Conhecimento do analista:** compreender os dados, regras de negócio, código e métricas.
- **Aceleração com IA:** utilizar a ferramenta para apoiar tarefas técnicas e reduzir trabalho repetitivo.
- **Validação humana:** conferir fórmulas, consultas, relacionamentos e resultados antes de utilizá-los.
- **Documentação:** registrar decisões, limitações e procedimentos relevantes para a reprodutibilidade.

A IA apoia o trabalho analítico, mas não substitui a compreensão técnica, a validação dos resultados ou a responsabilidade do analista.

## Conclusão

O **People Analytics RH** demonstra a integração de Python, PostgreSQL, SQL, modelagem analítica, DAX e Power BI em um cenário fictício de Recursos Humanos.

O projeto reúne preparação de dados, consultas analíticas, construção de indicadores, visualização e documentação em um fluxo de trabalho de ponta a ponta.

Seu propósito é demonstrar competências técnicas, raciocínio analítico, qualidade de implementação e comunicação de resultados, com transparência sobre o caráter sintético dos dados.

---

## Autor

**Renato Leone**  
Analista de Dados | Business Intelligence

- **GitHub:** [github.com/rrleone](https://github.com/rrleone)
- **Portfólio:** [Renato Leone — Data Analytics & BI](https://sites.google.com/view/renatoleone/)
- **Repositório:** [People_Analytics_RH](https://github.com/rrleone/People_Analytics_RH)

## Referências

**Documentação**

- [Python](https://docs.python.org/3/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Microsoft Power BI](https://learn.microsoft.com/power-bi/)
- [DAX — Microsoft Learn](https://learn.microsoft.com/dax/)

---

<div align="center">

**PEOPLE ANALYTICS RH**  
*Dados · Qualidade · Análise · Insights · Decisões*

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
