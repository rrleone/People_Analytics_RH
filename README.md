# 👥 People Analytics RH | Análise de Dados e Business Intelligence

<p align="center">
  <strong>Transformando dados de Recursos Humanos em indicadores para apoiar decisões de gestão.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Preparation-blue?logo=python" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql" />
  <img src="https://img.shields.io/badge/SQL-Analytics-orange" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi" />
  <img src="https://img.shields.io/badge/DAX-Analytics-yellow" />
</p>

> **Natureza do projeto:** laboratório educacional desenvolvido com dados fictícios e indicadores simulados. Os resultados não representam uma empresa real.

---

## 📌 Visão geral

O **People Analytics RH** é um projeto de estudo e portfólio desenvolvido para demonstrar um fluxo de trabalho de ponta a ponta em Análise de Dados e Business Intelligence aplicado ao contexto de Recursos Humanos.

O laboratório integra preparação e validação de dados com Python, armazenamento e consultas analíticas em PostgreSQL, exploração com SQL, modelagem e construção de dashboards no Power BI.

O objetivo é demonstrar competências técnicas, raciocínio analítico, qualidade de implementação e comunicação de resultados.

## 🎯 Problema de negócio

Em um cenário fictício de Recursos Humanos, a gestão precisa acompanhar:

- Composição e evolução do quadro de funcionários;
- Perfil dos colaboradores e distribuição organizacional;
- Custos e componentes da remuneração;
- Admissões e desligamentos;
- Indicadores de movimentação e rotatividade.

O projeto simula o desenvolvimento de uma solução analítica capaz de organizar essas informações e transformá-las em indicadores para apoiar a interpretação de cenários de gestão de pessoas.

## 🗂️ Dados utilizados

**Origem:** base sintética desenvolvida para fins educacionais.

| Tabela | Finalidade |
|---|---|
| `funcionarios` | Cadastro e características dos colaboradores fictícios |
| `eventos_rh` | Eventos simulados de admissão e desligamento |
| `historico_quadro_mensal` | Histórico mensal do quadro de funcionários |
| `historico_remuneracao` | Histórico mensal dos componentes remuneratórios |
| `dim_calendario` | Referência temporal |
| `dim_area` | Classificação das áreas organizacionais |
| `dim_cargo` | Classificação dos cargos |
| `dim_localidade` | Classificação das localidades |
| `dim_nivel` | Classificação dos níveis hierárquicos |

Os indicadores devem ser interpretados considerando as regras de negócio, os filtros e as limitações do cenário simulado.

## 🛠️ Tecnologias e ferramentas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Automação, preparação e validação dos dados |
| PostgreSQL | Armazenamento e consulta das tabelas |
| SQL | Exploração, agregações, análises temporais e funções de janela |
| Power BI | Modelagem analítica, dashboards e indicadores |
| DAX | Medidas e métricas analíticas |
| Git / GitHub | Versionamento e organização do portfólio |
| Inteligência Artificial | Apoio ao desenvolvimento, depuração e documentação, com validação humana |

## ⚙️ Metodologia

O desenvolvimento contempla as seguintes etapas:

1. **Data Profiling** — entendimento da estrutura, tipos e características dos dados.
2. **Data Quality** — verificações de valores ausentes, duplicidades, consistência e integridade.
3. **Data Preparation** — organização e preparação dos arquivos.
4. **Data Loading** — carga das tabelas no PostgreSQL.
5. **SQL Exploration** — exploração das entidades e estruturas de dados.
6. **Analytical Queries** — consultas sobre quadro de funcionários, movimentações, remuneração e qualidade.
7. **Data Modeling** — organização das tabelas, dimensões e relacionamentos.
8. **Power BI Data Modeling** — configuração do modelo analítico, calendário e medidas DAX.
9. **Dashboard & KPIs** — construção das páginas executivas e analíticas.
10. **Business Insights** — interpretação dos resultados do cenário simulado.
11. **AI-Assisted Analysis** — uso de IA como apoio, com revisão e validação humana.
12. **Documentation & Portfolio** — documentação técnica e organização dos materiais.

## 📊 Validação dos dados

Na consulta de perfil executada no PostgreSQL, foram registrados os seguintes resultados para a data de referência de **30/09/2026**:

| Indicador | Resultado |
|---|---:|
| Funcionários cadastrados | 600 |
| Funcionários ativos | 510 |
| Funcionários desligados | 90 |

A classificação considera a data de admissão e a situação do desligamento na data de referência.

Esses números pertencem exclusivamente à base sintética utilizada no laboratório.

A validação técnica também contempla verificações de integridade, consistência e relacionamento entre as tabelas.

---

## 📈 Dashboard Power BI

O relatório está organizado em quatro páginas, com perspectivas complementares de análise de Recursos Humanos.

### 01 — Visão Executiva

Consolidação dos principais indicadores do cenário simulado, permitindo uma visão geral da estrutura e situação do quadro de funcionários.

![Visão Executiva](<07_Portfolio/01 - VISÃO EXECUTIVA.png>)

### 02 — Perfil RH

Exploração do perfil dos colaboradores, distribuição organizacional e tempo de empresa.

![Perfil RH](<07_Portfolio/02 - PERFIL RH.png>)

### 03 — Remuneração

Análise dos custos de pessoal, composição remuneratória e indicadores relacionados à remuneração.

![Remuneração](<07_Portfolio/03 - REMUNERAÇÃO.png>)

### 04 — Turnover

Análise das movimentações simuladas de pessoal, incluindo admissões, desligamentos e indicadores de rotatividade.

![Turnover](<07_Portfolio/04 - TURNOVER.png>)

---

## 🔎 Perguntas analíticas exploradas

O laboratório permite investigar questões relevantes para gestão de pessoas:

- Como o quadro de funcionários evolui ao longo do período?
- Como os colaboradores se distribuem entre áreas, cargos e níveis?
- Qual é a composição dos custos de remuneração?
- Como admissões e desligamentos se distribuem ao longo do tempo?
- Qual é o perfil de tempo de empresa dos colaboradores?
- Quais indicadores merecem acompanhamento em um cenário de RH?

As conclusões devem ser fundamentadas nos dados, nas definições das métricas e nos filtros utilizados. Por se tratar de uma base sintética, não representam resultados reais de uma organização.

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

Os arquivos de dados locais não precisam ser publicados automaticamente. Sua inclusão deve considerar a utilidade para reprodução e a confirmação de que contêm somente dados sintéticos.

## 🚀 Como reproduzir o projeto

Para reproduzir o laboratório em outro ambiente:

1. Instale e configure Python e as dependências necessárias.
2. Instale o PostgreSQL e crie o banco `people_analytics_rh`.
3. Disponibilize os arquivos sintéticos necessários no ambiente local.
4. Configure os parâmetros de conexão sem inserir credenciais diretamente no código.
5. Execute `02_Python/carregar_csvs_postgresql_seguro_v2.py`, respeitando as verificações de segurança do script.
6. Consulte os arquivos SQL em `03_SQL/consultas/`.
7. Abra `05_PowerBI/People_analytics.pbix`.
8. Configure a conexão ao banco e atualize os dados.
9. Compare os indicadores do Power BI com as consultas de validação.

Os resultados podem variar conforme a versão dos arquivos, as transformações e a configuração do ambiente.

> **Segurança:** não publique credenciais, senhas, arquivos `.env` ou informações confidenciais.

## 🤖 Uso profissional de Inteligência Artificial

A IA foi utilizada como apoio ao desenvolvimento de scripts, consultas SQL, medidas, depuração e documentação.

O uso foi organizado em quatro dimensões:

- **Conhecimento do analista:** compreender os dados, regras de negócio, código e métricas.
- **Aceleração com IA:** apoiar tarefas técnicas e reduzir trabalho repetitivo.
- **Validação humana:** conferir fórmulas, consultas, relacionamentos e resultados.
- **Documentação:** registrar decisões, limitações e procedimentos relevantes.

A IA apoia o trabalho analítico, mas não substitui a compreensão técnica, a validação dos resultados ou a responsabilidade do analista.

## ✅ Conclusão

O **People Analytics RH** demonstra a integração de Python, PostgreSQL, SQL, modelagem analítica, DAX e Power BI em um cenário fictício de Recursos Humanos.

O projeto reúne preparação de dados, consultas analíticas, construção de indicadores, visualização e documentação em um fluxo de trabalho de ponta a ponta.

Seu propósito é demonstrar competências técnicas, raciocínio analítico, qualidade de implementação e comunicação de resultados, com transparência sobre o caráter sintético dos dados.

---

## 👤 Autor

**Renato Leone**  
Analista de Dados | Business Intelligence

[GitHub](https://github.com/rrleone) · [Portfólio](https://sites.google.com/view/renatoleone/)

<p align="center">
  <em>Dados • Análise • Insights • Decisões</em>
</p>
