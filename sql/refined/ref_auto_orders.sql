CREATE TABLE IF NOT EXISTS ref_auto_orders AS
SELECT 
    o.order_id,
    o.order_status,
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    i.product_id,
    i.price,
    i.freight_value
FROM raw_orders o
JOIN raw_order_items i ON o.order_id = i.order_id
JOIN raw_products p ON i.product_id = p.product_id
WHERE p.product_category_name = 'automotivo'
  AND o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL;