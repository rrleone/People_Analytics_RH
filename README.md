 <div align="center">

# PRIMECOMMERCE BI

### Análise Comercial · Desempenho de Vendas · Business Intelligence

**Projeto de Business Intelligence desenvolvido por Renato Leone**

Transformação de dados operacionais de e-commerce em indicadores, análises visuais e insights para apoiar a tomada de decisões comerciais.

![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Power Query](https://img.shields.io/badge/Power%20Query-ETL-217346?style=for-the-badge)
![DAX](https://img.shields.io/badge/DAX-Análise%20de%20Dados-2F80ED?style=for-the-badge)
![Business Intelligence](https://img.shields.io/badge/Business-Intelligence-267C78?style=for-the-badge)

</div>

---

## Visão geral do projeto

O **PrimeCommerce BI** é um projeto de Business Intelligence voltado à análise comercial de um e-commerce de pequeno porte.

O objetivo é transformar dados operacionais em informações estruturadas, indicadores e dashboards que permitam acompanhar o desempenho das vendas, compreender o comportamento dos clientes e identificar oportunidades de melhoria.

O projeto contempla perfilamento, qualidade e preparação dos dados, modelagem analítica, criação de indicadores com DAX e desenvolvimento de dashboards no Power BI.

![PrimeCommerce BI — Capa](03_Images/Capa%20PrimeCommerce%20BI%20com%20Dashboard%20de%20Vendas.png)

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

![PrimeCommerce BI — Visão Geral Comercial](03_Images/dashboard_visao_geral.png)

### 02 — Análise de Vendas

Análise da evolução temporal dos indicadores e comparação do desempenho entre os canais de venda.

- Evolução do Faturamento Mensal
- Evolução dos Pedidos Mensais
- Evolução do Ticket Médio Mensal
- Pedidos por Canal de Venda
- Faturamento por Canal de Venda
- Ticket Médio por Canal de Venda

![PrimeCommerce BI — Análise de Vendas](03_Images/dashboard_analise_vendas.png)

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

![PrimeCommerce BI — Clientes e Canais](03_Images/dashboard_clientes_canais.png)

## Problema de negócio e objetivos

A gestão da PrimeCommerce precisa acompanhar o desempenho comercial e compreender como o faturamento se distribui entre canais de venda, categorias de produtos e vendedores.

O projeto busca responder às seguintes questões:

- Quais canais apresentam maior faturamento e volume de pedidos?
- Quais categorias contribuem mais para o faturamento?
- Como faturamento, pedidos e ticket médio evoluem ao longo do tempo?
- Como os clientes se distribuem geograficamente?
- Qual é o nível de recorrência das compras?
- Existe concentração do faturamento nos principais clientes?

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

A página Clientes e Canais complementa essas análises com informações sobre recorrência, concentração do faturamento, distribuição geográfica e desempenho comercial.

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
│   ├── pedidos.csv
│   ├── itens_pedido.csv
│   ├── pagamentos.csv
│   └── entregas.csv
├── 02_Power_BI/
│   └── PrimeCommerce_BI.pbix
├── 03_Documentacao/
├── 04_Exportacoes/
├── 03_Images/
│   ├── Capa PrimeCommerce BI com Dashboard de Vendas.png
│   ├── dashboard_visao_geral.png
│   ├── dashboard_analise_vendas.png
│   └── dashboard_clientes_canais.png
└── README.md
```

## Como explorar o projeto

1. Clone ou baixe o repositório.
2. Acesse a pasta `02_Power_BI`.
3. Abra `PrimeCommerce_BI.pbix` no Power BI Desktop.
4. Verifique os caminhos das fontes de dados, caso necessário.
5. Atualize os dados utilizando a opção **Atualizar**.
6. Navegue pelas três páginas do relatório.

**Observação:** a reprodução poderá exigir ajustes nos caminhos dos arquivos de origem.

## Autor

**Renato Leone**  
Analista de Dados | Business Intelligence

- **GitHub:** [github.com/rrleone](https://github.com/rrleone)
- **Portfólio:** [Renato Leone — Data Analytics & BI](https://sites.google.com/view/renatoleone/)
- **Repositório:** [PrimeCommerce_BI](https://github.com/rrleone/PrimeCommerce_BI)

## Referências

**Documentação**

- [Microsoft Power BI](https://learn.microsoft.com/power-bi/)
- [Power Query](https://learn.microsoft.com/power-query/)
- [DAX — Microsoft Learn](https://learn.microsoft.com/dax/)

---

<div align="center">

**PRIMECOMMERCE BI**  
*Dados · Qualidade · Análise · Insights · Decisões*

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
