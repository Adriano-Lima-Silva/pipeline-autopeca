# 🚗 AutoParts Pipeline: Análise de Logística da Olist

## 🎯 Sobre o Projeto
Este pipeline de dados foi construído do zero utilizando o dataset público da Olist. O objetivo aqui foi nichar a análise: **filtrar exclusivamente o setor automotivo (autopeças)** para responder a duas perguntas cruciais para este mercado:
1. Qual o peso do frete no valor final de uma autopeça?
2. Como está a performance logística (atrasos) das entregas desse setor?

## 📊 A Fonte de Dados
- **Fonte**: [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Licença**: CC BY-NC-SA 4.0 (Permite uso público não-comercial).
- **Tabelas utilizadas**:
  - `olist_orders_dataset`: Cada linha é um pedido único feito por um cliente.
  - `olist_order_items_dataset`: Cada linha é um item (produto) dentro de um pedido.
  - `olist_products_dataset`: Cada linha é o cadastro e as dimensões de um produto específico.

## 🏗️ As Três Camadas
1. **Raw (Bruta)**: Os CSVs originais ingeridos integralmente no SQLite via Pandas (`raw_orders`, `raw_order_items`, `raw_products`). Nenhuma alteração foi feita.
2. **Refined (Tratada)**: A tabela `ref_auto_orders` limpa os dados, faz os JOINs entre pedidos, itens e produtos, e filtra *apenas* os pedidos com status 'delivered' da categoria 'automotivo'.
3. **Marts (Indicadores)**: 
   - `mart_freight_impact`: Indica a proporção do valor do frete em relação ao ticket médio da peça.
   - `mart_delivery_delay`: Calcula quantas entregas atrasaram e o tempo médio (em dias) de entrega.

## 🚀 Como rodar do zero

1. Clone este repositório.
2. Instale as dependências:
   `pip install -r requirements.txt`
3. Baixe os 3 CSVs do Kaggle e coloque na pasta `data/raw/`.
4. Rode a extração para a camada Raw:
   `python src/extract_load.py`
5. Rode as transformações (Refined e Marts):
   `python src/transform.py`
6. Para testar as regras de negócio de forma isolada (testes unitários com mock data):
   `pytest tests/`

## 🤖 Uso de Inteligência Artificial
A IA (LLM) foi utilizada para auxiliar na escrita das queries SQL e na estruturação do repositório. 

**Onde a IA errou e como descobri:**
Ao pedir para a IA gerar a query do indicador de tempo médio de entrega no `mart_delivery_delay.sql`, ela sugeriu a sintaxe padrão ANSI: 
`AVG(order_delivered_customer_date - order_purchase_timestamp)`.
Descobri o erro executando o script e notando que o SQLite não lida com subtração direta de datas (timestamps como strings), retornando valores numéricos não correspondentes a dias. Corrigi o código substituindo a lógica direta por funções nativas do SQLite, utilizando `AVG(julianday(...) - julianday(...))`, o que resolveu o problema e trouxe a diferença exata em dias.
