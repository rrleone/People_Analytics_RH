# 👥 People Analytics RH | Laboratório de Análise de Dados

Projeto de estudo e portfólio desenvolvido para praticar um fluxo de trabalho de ponta a ponta em Análise de Dados e Business Intelligence aplicado ao contexto de Recursos Humanos.

> **Natureza do projeto:** laboratório educacional com dados fictícios e indicadores simulados. Os resultados não representam uma empresa real.

---

## 🎯 Problema de negócio simulado

Em um cenário fictício de Recursos Humanos, a gestão precisa acompanhar a composição do quadro de funcionários, o perfil dos colaboradores, os custos de remuneração e as movimentações de pessoal.

Este projeto simula o desenvolvimento de uma solução analítica para organizar essas informações, construir indicadores e apresentar resultados que apoiem a interpretação de cenários de gestão de pessoas.

O objetivo técnico é demonstrar como dados estruturados podem ser preparados, validados, consultados, modelados e apresentados por meio de ferramentas de Análise de Dados e Business Intelligence.

---

## 🗂️ Sobre os dados

- **Origem:** base sintética desenvolvida para fins educacionais.
- **Domínio:** People Analytics / Recursos Humanos.
- **Tipo de análise:** Análise de Dados e Business Intelligence.
- **Banco de dados:** PostgreSQL.
- **Preparação e validação:** Python.
- **Consultas analíticas:** SQL.
- **Visualização:** Power BI.
- **Versionamento:** Git e GitHub.

### Conjuntos de dados

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

---

## 🛠️ Ferramentas utilizadas

- **Python:** automação e validação dos dados.
- **PostgreSQL:** armazenamento e consulta das tabelas.
- **SQL:** exploração, agregações, análises temporais e funções de janela.
- **Power BI:** construção dos dashboards e apresentação dos indicadores.
- **DAX:** criação de medidas e indicadores analíticos.
- **Git / GitHub:** versionamento e publicação do portfólio.
- **Inteligência Artificial:** apoio ao desenvolvimento, à depuração e à documentação, com validação humana.

---

## 🔍 Etapas do projeto

1. **Data Profiling** — entendimento da estrutura, dos tipos e das características dos dados.
2. **Data Quality** — verificações de valores ausentes, duplicidades, consistência e integridade.
3. **Data Preparation** — organização e preparação dos arquivos para análise.
4. **Data Loading** — carga das tabelas no PostgreSQL.
5. **SQL Exploration** — exploração dos dados e compreensão das entidades.
6. **Analytical Queries** — consultas para análise do quadro de funcionários, movimentações, remuneração e qualidade dos dados.
7. **Data Modeling** — organização das tabelas, dimensões e relacionamentos.
8. **Power BI Data Modeling** — configuração do modelo analítico, calendário e medidas DAX.
9. **Dashboard & KPIs** — construção das páginas executivas e analíticas.
10. **Business Insights** — interpretação dos resultados e identificação de pontos de atenção no cenário simulado.
11. **AI-Assisted Analysis** — utilização de IA como apoio, com revisão e validação pelo analista.
12. **Documentation & Portfolio** — documentação técnica e organização dos materiais de apresentação.

As etapas descrevem o fluxo de trabalho planejado e desenvolvido no laboratório. A conclusão de cada análise depende da validação dos respectivos resultados.

---

## 📊 Indicadores e validações

Na consulta de perfil executada no PostgreSQL, foram registrados os seguintes resultados para a data de referência de **30/09/2026**:

| Indicador | Resultado registrado |
|---|---:|
| Funcionários cadastrados | 600 |
| Funcionários ativos | 510 |
| Funcionários desligados | 90 |

Esses valores correspondem à base sintética utilizada durante o desenvolvimento e não representam estatísticas de uma empresa real.

A classificação considera a data de admissão e a situação do desligamento na data de referência. A interpretação dos indicadores depende das regras de negócio e dos filtros aplicados.

A validação técnica também contempla verificações de integridade, consistência e relacionamento entre as tabelas.

---

## 🖼️ Prévia do dashboard

O relatório desenvolvido no Power BI está organizado em quatro páginas.

### 01 — Visão Executiva

Apresentação consolidada dos principais indicadores do cenário simulado de Recursos Humanos.

### 02 — Perfil RH

Exploração do perfil dos colaboradores, da distribuição organizacional e do tempo de empresa.

### 03 — Remuneração

Análise dos custos de pessoal, da composição remuneratória e dos indicadores relacionados à remuneração.

### 04 — Turnover

Análise das movimentações simuladas de pessoal, incluindo admissões, desligamentos e indicadores de rotatividade.

As capturas de tela estão organizadas na pasta `07_Portfolio/`.

---

## 📈 Análises e oportunidades

O laboratório permite explorar perguntas como:

- Como o quadro de funcionários evolui ao longo do período analisado?
- Como os colaboradores se distribuem entre áreas, cargos e níveis?
- Qual é a composição dos custos de remuneração?
- Como as admissões e os desligamentos se distribuem ao longo do tempo?
- Qual é o perfil de tempo de empresa dos colaboradores?
- Quais indicadores merecem acompanhamento em um cenário de gestão de pessoas?

As respostas devem ser fundamentadas nos dados, nas definições das métricas e nos filtros utilizados. Como se trata de uma base sintética, as conclusões servem para demonstrar métodos de análise, e não para afirmar resultados reais sobre uma organização.

---

## 📁 Estrutura do repositório

```text
People_Analytics_RH/
│
├── 01_Dados/
│   ├── 01_Originais/
│   ├── 02_Tratados/
│   └── 03_Validacao/
│
├── 02_Python/
│   ├── carregar_csvs_postgresql_seguro_v2.py
│   └── validar_base_people_analytics.py
│
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
│
├── 04_Modelagem/
│   └── README.md
│
├── 05_PowerBI/
│   └── People_analytics.pbix
│
├── 06_Documentacao/
│   ├── Guia_Comandos_People_Analytics_RH.pdf
│   └── Relatorio_Processo_People_Analytics_RH.pdf
│
├── 07_Portfolio/
│   ├── 01 - VISÃO EXECUTIVA.png
│   ├── 02 - PERFIL RH.png
│   ├── 03 - REMUNERAÇÃO.png
│   └── 04 - TURNOVER.png
│
├── .gitignore
└── README.md
```

A árvore apresenta a organização esperada dos principais arquivos. Os arquivos de dados locais não precisam ser publicados automaticamente: sua inclusão deve considerar a utilidade para reprodução, a consistência entre versões e a confirmação de que contêm somente dados sintéticos.

---

## 🚀 Como reproduzir

Para reproduzir o laboratório em outro ambiente:

1. Instale e configure o Python e as dependências necessárias.
2. Instale o PostgreSQL e crie o banco `people_analytics_rh`.
3. Disponibilize os arquivos sintéticos necessários no ambiente local.
4. Configure os parâmetros de conexão sem inserir senhas ou credenciais no código.
5. Execute `02_Python/carregar_csvs_postgresql_seguro_v2.py`, respeitando as verificações de segurança do script.
6. Consulte os arquivos SQL de `03_SQL/consultas/` e execute as análises conforme suas dependências.
7. Abra `05_PowerBI/People_analytics.pbix`.
8. Configure a conexão ao banco e atualize os dados.
9. Confira os indicadores apresentados e compare-os com as consultas de validação.

Os resultados podem variar conforme a versão dos arquivos, as regras de transformação e a configuração do ambiente.

**Segurança:** não publique credenciais, senhas, arquivos `.env` ou informações confidenciais.

---

## 🤖 Uso profissional de Inteligência Artificial

A IA foi utilizada como apoio ao desenvolvimento de scripts, consultas SQL, medidas, depuração e documentação.

O uso profissional da ferramenta é organizado em quatro dimensões:

1. **Conhecimento do analista:** compreender os dados, as regras de negócio, o código e as métricas.
2. **Aceleração com IA:** utilizar a ferramenta para apoiar tarefas técnicas e reduzir trabalho repetitivo.
3. **Validação humana:** conferir fórmulas, consultas, relacionamentos e resultados antes de utilizá-los.
4. **Documentação:** registrar decisões, limitações e procedimentos relevantes para a reprodutibilidade.

A IA apoia o trabalho analítico, mas não substitui a compreensão técnica, a validação dos resultados ou a responsabilidade do analista.

---

## ✅ Conclusão

O People Analytics RH é um laboratório de estudo que demonstra a integração de Python, PostgreSQL, SQL, modelagem analítica, DAX e Power BI em um cenário fictício de Recursos Humanos.

O projeto reúne preparação de dados, consultas analíticas, construção de indicadores, visualização e documentação em um fluxo de trabalho de ponta a ponta.

Seu propósito é demonstrar competências técnicas, raciocínio analítico, qualidade de implementação e comunicação de resultados, com transparência sobre o caráter sintético dos dados.

---

## 👤 Autor

**Renato Leone**

Analista de Dados | Business Intelligence

GitHub: https://github.com/rrleone
