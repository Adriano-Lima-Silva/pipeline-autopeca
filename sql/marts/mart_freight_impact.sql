CREATE TABLE IF NOT EXISTS mart_freight_impact AS
SELECT 
    COUNT(order_id) as total_pedidos_auto,
    AVG(price) as ticket_medio_peca,
    AVG(freight_value) as frete_medio,
    (AVG(freight_value) / AVG(price)) * 100 as percentual_frete_sobre_peca
FROM ref_auto_orders;