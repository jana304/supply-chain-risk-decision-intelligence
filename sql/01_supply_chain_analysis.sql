USE supply_chain_risk;

SELECT
    `Shipping Mode`,
    COUNT(*) AS total_order_items,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY `Shipping Mode`
ORDER BY late_risk_rate DESC;

SELECT
    `Order Region`,
    COUNT(*) AS total_order_items,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY `Order Region`
ORDER BY late_risk_rate DESC;

SELECT
    `Order Region`,
    `Shipping Mode`,
    COUNT(*) AS total_order_items,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY
    `Order Region`,
    `Shipping Mode`
HAVING COUNT(*) >= 100
ORDER BY late_risk_rate DESC;

SELECT
    `Late_delivery_risk`,
    COUNT(*) AS total_order_items,
    ROUND(SUM(`Sales`), 2) AS total_sales,
    ROUND(SUM(`Order Profit Per Order`), 2) AS total_profit,
    ROUND(
        SUM(`Sales`) * 100.0 /
        (SELECT SUM(`Sales`) FROM supply_chain_data),
        2
    ) AS sales_percentage
FROM supply_chain_data
GROUP BY `Late_delivery_risk`
ORDER BY `Late_delivery_risk` DESC;

SELECT
    `Department Name`,
    COUNT(*) AS total_order_items,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(`Sales`), 2
    ) AS total_sales,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY `Department Name`
ORDER BY late_risk_rate DESC;

SELECT
    `Shipping Mode`,
    `Department Name`,
    COUNT(*) AS total_order_items,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY
    `Shipping Mode`,
    `Department Name`
HAVING COUNT(*) >= 100
ORDER BY late_risk_rate DESC;

SELECT
    `Shipping Mode`,
    COUNT(*) AS total_order_items,
    ROUND(SUM(`Sales`), 2) AS total_sales,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(
            CASE
                WHEN `Late_delivery_risk` = 1
                THEN `Sales`
                ELSE 0
            END
        ),
        2
    ) AS sales_at_risk,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY `Shipping Mode`
ORDER BY sales_at_risk DESC;

SELECT
    `Market`,
    COUNT(*) AS total_order_items,
    ROUND(SUM(`Sales`), 2) AS total_sales,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(
            CASE
                WHEN `Late_delivery_risk` = 1
                THEN `Sales`
                ELSE 0
            END
        ),
        2
    ) AS sales_at_risk,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY `Market`
ORDER BY sales_at_risk DESC;

SELECT
    `Shipping Mode`,
    `Market`,
    COUNT(*) AS total_order_items,
    ROUND(SUM(`Sales`), 2) AS total_sales,
    SUM(`Late_delivery_risk`) AS late_risk_items,
    ROUND(
        SUM(
            CASE
                WHEN `Late_delivery_risk` = 1
                THEN `Sales`
                ELSE 0
            END
        ),
        2
    ) AS sales_at_risk,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate
FROM supply_chain_data
GROUP BY
    `Shipping Mode`,
    `Market`
HAVING COUNT(*) >= 100
ORDER BY
    sales_at_risk DESC;

SELECT
    `Shipping Mode`,
    `Market`,
    ROUND(
        SUM(
            CASE
                WHEN `Late_delivery_risk` = 1
                THEN `Sales`
                ELSE 0
            END
        ),
        2
    ) AS sales_at_risk,
    ROUND(
        SUM(`Late_delivery_risk`) * 100.0 / COUNT(*),
        2
    ) AS late_risk_rate,
    COUNT(*) AS total_order_items
FROM supply_chain_data
GROUP BY
    `Shipping Mode`,
    `Market`
HAVING COUNT(*) >= 100
ORDER BY
    late_risk_rate DESC,
    sales_at_risk DESC;