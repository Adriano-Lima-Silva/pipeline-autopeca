CREATE TABLE IF NOT EXISTS mart_delivery_delay AS
SELECT 
    SUM(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 ELSE 0 END) as entregas_atrasadas,
    SUM(CASE WHEN order_delivered_customer_date <= order_estimated_delivery_date THEN 1 ELSE 0 END) as entregas_no_prazo,
    AVG(julianday(order_delivered_customer_date) - julianday(order_purchase_timestamp)) as tempo_medio_entrega_dias
FROM ref_auto_orders;