# 👥 People Analytics RH

Projeto de Análise de Dados e Business Intelligence aplicado à gestão de Recursos Humanos, integrando Python, PostgreSQL, SQL e Power BI para transformar dados de colaboradores em indicadores e informações de apoio à decisão.

## 🎯 Problema de negócio

A gestão de Recursos Humanos envolve acompanhar a composição do quadro de funcionários, o perfil dos colaboradores, os custos de remuneração e a movimentação de pessoas.

Este projeto tem como objetivo estruturar uma solução analítica que permita acompanhar indicadores de pessoal, compreender a evolução do quadro de funcionários e apoiar análises relacionadas a admissões, desligamentos, remuneração e tempo de empresa.

A proposta é demonstrar um fluxo de trabalho de ponta a ponta, desde a preparação e validação dos dados até a modelagem analítica e a apresentação de indicadores em dashboards executivos.

---

## 🗂️ Sobre os dados

- **Domínio:** People Analytics / Recursos Humanos
- **Tipo de análise:** Análise de Dados e Business Intelligence
- **Banco de dados:** PostgreSQL
- **Linguagem de consulta:** SQL
- **Preparação e validação:** Python
- **Visualização:** Power BI
- **Versionamento:** Git e GitHub

### Principais conjuntos de dados

| Conjunto de dados | Finalidade |
|---|---|
| `funcionarios` | Cadastro e informações dos colaboradores |
| `eventos_rh` | Eventos de admissão e desligamento |
| `historico_quadro_mensal` | Histórico mensal do quadro de funcionários |
| `historico_remuneracao` | Histórico mensal dos componentes de remuneração |
| `dim_calendario` | Referência temporal para as análises |
| `dim_area` | Classificação das áreas organizacionais |
| `dim_cargo` | Classificação dos cargos |
| `dim_localidade` | Informações geográficas |
| `dim_nivel` | Classificação dos níveis hierárquicos |

Os arquivos tratados são mantidos localmente e não fazem parte da publicação do repositório, em razão da necessidade de proteger os dados dos colaboradores.

---

## 🛠️ Ferramentas utilizadas

- **Python:** automação de verificações e validação dos dados.
- **PostgreSQL:** armazenamento e consulta dos dados.
- **SQL:** exploração, agregações, análise temporal, funções de janela e consultas analíticas.
- **Power BI:** construção dos dashboards e acompanhamento dos indicadores.
- **DAX:** criação de medidas e indicadores para análise de Recursos Humanos.
- **Git / GitHub:** versionamento, documentação e organização do portfólio.
- **Inteligência Artificial:** apoio ao desenvolvimento, à depuração e à documentação, com validação humana.

---

## 🔍 Etapas do projeto

1. **Data Profiling** — entendimento da estrutura, dos tipos de dados e das características das tabelas.
2. **Data Quality** — verificações de valores ausentes, duplicidades, consistência e integridade.
3. **Data Preparation** — organização dos arquivos e preparação dos dados para análise.
4. **Data Loading** — carga dos conjuntos de dados no PostgreSQL.
5. **SQL Exploration** — consultas exploratórias e análise das informações de Recursos Humanos.
6. **Analytical Queries** — desenvolvimento de consultas para quadro de funcionários, movimentações, remuneração e qualidade dos dados.
7. **Data Modeling** — organização das tabelas, relacionamentos e dimensões analíticas.
8. **Power BI Data Modeling** — configuração do modelo, calendário, relacionamentos e medidas DAX.
9. **Dashboard & KPIs** — construção de páginas executivas e analíticas.
10. **Business Insights** — interpretação dos indicadores e identificação de pontos de atenção.
11. **AI-Assisted Analysis** — utilização de IA como apoio, com revisão e validação pelo analista.
12. **Documentation & Portfolio** — organização dos scripts, documentação técnica e apresentação do projeto.

As etapas representam o fluxo de trabalho do projeto. A conclusão de cada análise deve ser considerada conforme seus respectivos resultados e validações.

---

## 📊 Indicadores e validações

Na consulta de perfil dos funcionários executada no PostgreSQL, foram registrados os seguintes resultados, considerando a referência de **30/09/2026**:

| Indicador | Resultado |
|---|---:|
| Total de funcionários cadastrados | 600 |
| Funcionários ativos | 510 |
| Funcionários desligados | 90 |

Esses valores correspondem à consulta executada no banco de dados durante o desenvolvimento.

A classificação de funcionários ativos considera a data de admissão e a situação do desligamento na data de referência. Os indicadores devem ser interpretados conforme as regras de negócio e os filtros utilizados.

A validação técnica também contempla verificações de integridade, consistência e relacionamento entre as tabelas.

---

## 🖼️ Prévia do dashboard

O relatório desenvolvido no Power BI possui quatro páginas:

### 01 — Visão Executiva

Visão consolidada dos principais indicadores de Recursos Humanos, com foco no acompanhamento do quadro de funcionários e dos resultados gerais.

### 02 — Perfil RH

Análise do perfil dos colaboradores, incluindo características organizacionais, níveis hierárquicos e tempo de empresa.

### 03 — Remuneração

Acompanhamento dos custos de pessoal, composição da remuneração e indicadores relacionados aos valores remuneratórios.

### 04 — Turnover

Análise das movimentações de pessoal, com acompanhamento de admissões, desligamentos e indicadores relacionados à rotatividade.

As capturas das páginas estão disponíveis na pasta `07_Portfolio/`.

---

## 📈 Análises e oportunidades

A estrutura analítica permite explorar questões relevantes para a gestão de pessoas, como:

- Como o quadro de funcionários evolui ao longo do tempo?
- Como os colaboradores estão distribuídos entre áreas, cargos e níveis?
- Qual é a composição dos custos de remuneração?
- Como as admissões e os desligamentos se distribuem ao longo dos períodos?
- Qual é o perfil de tempo de empresa dos colaboradores?
- Quais indicadores merecem acompanhamento pela gestão de Recursos Humanos?

As respostas devem ser fundamentadas nos dados, nas definições das métricas e nos filtros aplicados. Associações observadas não representam, por si só, relações de causalidade.

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
│   ├── consultas/
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

A estrutura apresenta os principais diretórios e arquivos do repositório. Os arquivos CSV de dados e os relatórios locais de validação são excluídos da publicação.

---

## 🚀 Como reproduzir

Para reproduzir o fluxo de trabalho em outro ambiente:

1. Configure o Python e as dependências necessárias para executar os scripts.
2. Configure o PostgreSQL e crie o banco de dados `people_analytics_rh`.
3. Disponibilize localmente os arquivos de dados autorizados para uso.
4. Configure as credenciais de conexão por meio do ambiente local, sem inseri-las no código ou no repositório.
5. Execute o script `02_Python/carregar_csvs_postgresql_seguro_v2.py`, respeitando as verificações de segurança implementadas.
6. Execute as consultas SQL em `03_SQL/consultas/` conforme suas dependências.
7. Abra `05_PowerBI/People_analytics.pbix` e configure a conexão ao banco de dados do ambiente.
8. Atualize os dados e confira os indicadores apresentados no relatório.

Os resultados podem variar conforme a versão dos dados, as regras de transformação e a configuração do ambiente.

**Segurança:** não publique dados pessoais de colaboradores, senhas, credenciais, arquivos `.env` ou informações confidenciais.

---

## 🤖 Uso profissional de Inteligência Artificial

A Inteligência Artificial foi incorporada ao fluxo de desenvolvimento como ferramenta de apoio à programação, à elaboração de consultas SQL, à revisão de medidas, à depuração e à documentação.

O uso profissional de IA neste projeto considera quatro responsabilidades:

1. **Conhecimento do analista:** compreender os dados, as regras de negócio, o código e as métricas utilizadas.
2. **Aceleração com IA:** utilizar a ferramenta para apoiar tarefas técnicas e reduzir trabalho repetitivo.
3. **Validação humana:** verificar consultas, fórmulas, relacionamentos e resultados antes de utilizá-los em análises.
4. **Documentação:** registrar decisões, limitações e procedimentos relevantes para garantir transparência e reprodutibilidade.

A IA atua como apoio ao trabalho analítico. A responsabilidade pela qualidade dos dados, pela validação dos resultados e pela interpretação de negócio permanece com o analista.

---

## ✅ Conclusão

O People Analytics RH demonstra a aplicação integrada de preparação de dados, Python, PostgreSQL, SQL, modelagem analítica, DAX e Power BI em um contexto de Recursos Humanos.

O projeto reúne componentes técnicos e analíticos para transformar dados estruturados em indicadores que apoiam o acompanhamento do quadro de funcionários, da remuneração e das movimentações de pessoal.

Além da construção do dashboard, a iniciativa valoriza a qualidade dos dados, a documentação, a reprodutibilidade e o uso responsável da Inteligência Artificial.

---

## 👤 Autor

**Renato Leone**

Analista de Dados | Business Intelligence

GitHub: https://github.com/rrleone
