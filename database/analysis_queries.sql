-- Pure SQL Analysis Queries for B2B Regional Market Penetration & Service Performance

-- 1. Area-wise Total Sales and Transaction Count
SELECT 
    a.area_id,
    a.taluka,
    a.area_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.sales_amount) AS total_sales_amount,
    AVG(t.sales_amount) AS avg_transaction_value
FROM areas a
LEFT JOIN transactions t ON a.area_id = t.area_id
GROUP BY a.area_id, a.taluka, a.area_name
ORDER BY total_sales_amount DESC;

-- 2. Customer Market Penetration Analysis by Area
SELECT 
    a.area_id,
    a.taluka,
    a.estimated_industrial_units,
    COUNT(DISTINCT c.customer_id) AS active_customers,
    ROUND(
        (COUNT(DISTINCT c.customer_id) * 100.0 / a.estimated_industrial_units), 2
    ) AS market_penetration_pct,
    ROUND(
        (100.0 - (COUNT(DISTINCT c.customer_id) * 100.0 / a.estimated_industrial_units)), 2
    ) AS penetration_gap_pct
FROM areas a
LEFT JOIN customers c ON a.area_id = c.area_id
GROUP BY a.area_id, a.taluka, a.estimated_industrial_units
ORDER BY market_penetration_pct ASC;

-- 3. Dealer Capacity & Coverage Density by Area
SELECT 
    a.area_id,
    a.taluka,
    COUNT(DISTINCT d.dealer_id) AS active_dealer_count,
    a.estimated_industrial_units,
    ROUND(
        (COUNT(DISTINCT d.dealer_id) * 100.0 / a.estimated_industrial_units), 2
    ) AS dealers_per_100_units
FROM areas a
LEFT JOIN dealers d ON a.area_id = d.area_id AND d.active_status = 'Active'
GROUP BY a.area_id, a.taluka, a.estimated_industrial_units
ORDER BY active_dealer_count ASC;

-- 4. Service Delay and Delivery Performance by Area
SELECT 
    a.area_id,
    a.taluka,
    COUNT(s.service_id) AS total_deliveries,
    AVG(s.delivery_delay_days) AS avg_delivery_delay_days,
    AVG(s.response_time_hours) AS avg_response_time_hours,
    SUM(s.service_delay_flag) AS total_delayed_deliveries,
    ROUND(
        (SUM(s.service_delay_flag) * 100.0 / COUNT(s.service_id)), 2
    ) AS service_delay_pct
FROM areas a
LEFT JOIN service_records s ON a.area_id = s.area_id
GROUP BY a.area_id, a.taluka
ORDER BY avg_delivery_delay_days DESC;

-- 5. Industry-wise Revenue Breakdown across Top Untapped Areas
SELECT 
    a.taluka,
    c.industry_type,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    SUM(t.sales_amount) AS industry_sales
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
JOIN areas a ON t.area_id = a.area_id
GROUP BY a.taluka, c.industry_type
ORDER BY a.taluka, industry_sales DESC;
