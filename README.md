 <div align="center">

# 📊 PRIMECommerce BI

### Commercial Analytics · Sales Performance · Business Intelligence

**Business Intelligence project developed by Renato Leone**

Transforming e-commerce operational data into indicators, visual analyses and insights to support commercial decision-making.

![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Power Query](https://img.shields.io/badge/Power%20Query-ETL-217346?style=for-the-badge)
![DAX](https://img.shields.io/badge/DAX-Data%20Analysis-2F80ED?style=for-the-badge)
![Business Intelligence](https://img.shields.io/badge/Business-Intelligence-267C78?style=for-the-badge)

</div>

---

## Visão geral do projeto

O **PrimeCommerce BI** é um projeto de Business Intelligence voltado à análise comercial de um e-commerce de pequeno porte.

O objetivo é transformar dados operacionais em informações estruturadas, indicadores e dashboards que permitam acompanhar o desempenho das vendas, compreender o comportamento dos clientes e identificar oportunidades de melhoria.

O projeto contempla etapas de perfilamento, qualidade e preparação dos dados, modelagem analítica, criação de indicadores com DAX e desenvolvimento de dashboards no Power BI.

![Capa PrimeCommerce BI](05_Images/Capa%20PrimeCommerce%20BI%20com%20Dashboard%20de%20Vendas.png)

## Dashboards

O relatório Power BI está organizado em três páginas analíticas.

### 01 — Visão Geral Comercial

Painel executivo para acompanhamento dos principais indicadores de desempenho comercial.

- Faturamento Total
- Pedidos Totais
- Quantidade de Itens
- Ticket Médio
- Lucro Bruto
- Faturamento por Categoria
- Faturamento por Vendedor
- Faturamento por Canal de Venda

![PrimeCommerce BI — Visão Geral Comercial](images/dashboard_visao_geral.png)

### 02 — Análise de Vendas

Análise da evolução temporal dos indicadores e comparação do desempenho entre os canais de venda.

- Evolução do Faturamento Mensal
- Evolução dos Pedidos Mensais
- Evolução do Ticket Médio Mensal
- Pedidos por Canal de Venda
- Faturamento por Canal de Venda
- Ticket Médio por Canal de Venda

![PrimeCommerce BI — Análise de Vendas](images/dashboard_analise_vendas.png)

### 03 — Clientes e Canais

Análise do comportamento dos clientes, recorrência de compras, distribuição geográfica e desempenho dos canais.

- Clientes Únicos
- Clientes Recorrentes
- Faturamento por Cliente
- Pedidos por Cliente
- Faturamento por Estado e Cidade
- Jornada de Recorrência dos Clientes
- Desempenho dos Canais de Venda
- Top 5 Clientes por Faturamento
- Clientes Únicos por Cidade
- Participação dos cinco principais clientes no faturamento

![PrimeCommerce BI — Clientes e Canais](images/dashboard_clientes_canais.png)

## Problema de negócio e objetivos

A gestão da PrimeCommerce precisa acompanhar o desempenho comercial e compreender como o faturamento se distribui entre canais de venda, categorias de produtos e vendedores.

O projeto busca responder a questões como:

- Quais canais apresentam maior faturamento e volume de pedidos?
- Quais categorias de produtos contribuem mais para o faturamento?
- Como o faturamento, os pedidos e o ticket médio evoluem ao longo do tempo?
- Como os clientes se distribuem geograficamente?
- Qual é o nível de recorrência das compras?
- Existe concentração de faturamento nos principais clientes?

**Objetivo:** transformar dados operacionais em indicadores e análises visuais que apoiem o acompanhamento do desempenho e a tomada de decisões comerciais.

## Dados utilizados

- **Fonte:** dados simulados para estudo e portfólio
- **Segmento:** e-commerce
- **Período:** janeiro a agosto de 2026
- **Registros:** 1.492, conforme documentação da base de origem
- **Formato:** CSV

### Tabelas utilizadas

- `clientes`
- `produtos`
- `vendedores`
- `pedidos`
- `itens_pedido`
- `pagamentos`
- `entregas`

Os dados são fictícios e não representam uma empresa real.

## Metodologia analítica

O projeto foi desenvolvido seguindo um fluxo de trabalho de Business Intelligence.

**Fluxo:** Dados → Qualidade → Tratamento → Modelagem → Indicadores → Dashboards → Insights

### 1. Perfilamento e qualidade dos dados

Foram verificadas:

- Quantidade de registros e tipos de dados
- Valores nulos e inválidos
- Espaços extras em textos
- Unicidade das chaves
- Integridade referencial entre tabelas

Durante o perfilamento, foram identificadas ocorrências como valores nulos, quantidades inválidas, preços unitários negativos, datas inconsistentes e registros sem correspondência em algumas chaves.

### 2. Preparação e tratamento

O tratamento foi realizado no Power Query, incluindo:

- Preenchimento controlado de valores nulos com `Não informado`
- Correção de quantidades inválidas
- Correção de preços unitários com referência ao cadastro de produtos
- Correção de datas de entrega inconsistentes
- Remoção de espaços extras em campos textuais
- Consultas de QA para validação de registros sem correspondência

### 3. Modelagem de dados

Foram estruturados relacionamentos entre:

- Clientes e pedidos
- Vendedores e pedidos
- Pedidos e itens do pedido
- Produtos e itens do pedido
- Pedidos e pagamentos
- Pedidos e entregas

### 4. Indicadores e métricas

Foram desenvolvidos indicadores utilizando DAX:

- Faturamento Total
- Pedidos Totais
- Quantidade de Itens
- Ticket Médio
- Faturamento Concluído
- Custo Total
- Lucro Bruto

Também foi criada a coluna calculada `Custo_Total`, considerando a quantidade de itens e o custo unitário dos produtos.

## Principais insights

As análises documentadas no projeto identificaram:

- O **Site** apresenta o maior faturamento e o maior volume de pedidos entre os canais analisados.
- **Escritório** é a categoria com maior faturamento.
- **Março** apresenta o menor faturamento do período.
- Em março, o volume de pedidos permanece elevado, mas o ticket médio é o menor do período, contribuindo para o menor faturamento mensal.
- **Maio** apresenta o maior faturamento e o maior ticket médio mensal.
- **Marketplace** apresenta o maior ticket médio entre os canais de venda.

A análise de Clientes e Canais amplia a compreensão sobre recorrência, concentração do faturamento, distribuição geográfica e desempenho comercial.

## Tecnologias e ferramentas

| Tecnologia | Aplicação no projeto |
|---|---|
| Microsoft Power BI | Desenvolvimento dos dashboards e visualização analítica |
| Power Query (M) | Perfilamento, preparação e transformação dos dados |
| DAX | Criação de medidas, métricas e indicadores |
| Modelagem de dados | Organização das tabelas e relacionamentos |
| GitHub | Versionamento e documentação do projeto |

## Estrutura do repositório

```text
PrimeCommerce_BI/
├── 01_Dados_Raw/
│   ├── clientes.csv
│   ├── produtos.csv
│   ├── vendedores.csv
│  
