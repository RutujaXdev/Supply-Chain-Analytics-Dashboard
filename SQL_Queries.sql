-- =====================================================
-- KPI QUERIES
-- =====================================================

-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total Sales
SELECT SUM(sales) AS total_sales
FROM orders;

-- Total Profit
SELECT SUM(profit) AS total_profit
FROM orders;

-- Total Customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Average Order Value
SELECT ROUND(AVG(sales), 2) AS average_order_value
FROM orders;

-- Total Quantity Sold
SELECT SUM(quantity) AS total_quantity_sold
FROM orders;

-- Average Delivery Days
SELECT ROUND(AVG(delivery_days), 2) AS average_delivery_days
FROM orders;
-- =====================================================
-- SALES ANALYSIS
-- =====================================================

-- Sales by Category
SELECT
    p.category,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

-- Monthly Sales Trend
SELECT
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(sales) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;

-- Top 10 Products by Sales
SELECT
    p.product_name,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Top 10 Customers by Sales
SELECT
    c.customer_name,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by State
SELECT
    c.state,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.state
ORDER BY total_sales DESC;

-- Sales by Payment Method
SELECT
    payment_method,
    SUM(sales) AS total_sales
FROM orders
GROUP BY payment_method
ORDER BY total_sales DESC;
-- =====================================================
-- INVENTORY ANALYSIS
-- =====================================================

-- Inventory Quantity by Warehouse
SELECT
    w.warehouse_name,
    SUM(o.quantity) AS total_quantity
FROM orders o
JOIN warehouses w
ON o.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name
ORDER BY total_quantity DESC;

-- Products by Category
SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;

-- Warehouse Capacity
SELECT
    warehouse_name,
    capacity
FROM warehouses
ORDER BY capacity DESC;

-- Top 10 Products by Quantity Sold
SELECT
    p.product_name,
    SUM(o.quantity) AS quantity_sold
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY quantity_sold DESC
LIMIT 10;

-- Inventory Value by Product
SELECT
    p.product_name,
    SUM(o.quantity * o.cost_price) AS inventory_value
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY inventory_value DESC;
-- =====================================================
-- LOGISTICS ANALYSIS
-- =====================================================

-- Order Status Distribution
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- Shipping Cost by State
SELECT
    c.state,
    SUM(o.shipping_cost) AS total_shipping_cost
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.state
ORDER BY total_shipping_cost DESC;

-- Average Delivery Days by State
SELECT
    c.state,
    ROUND(AVG(o.delivery_days), 2) AS average_delivery_days
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.state
ORDER BY average_delivery_days;

-- Shipping Cost by Payment Method
SELECT
    payment_method,
    SUM(shipping_cost) AS total_shipping_cost
FROM orders
GROUP BY payment_method
ORDER BY total_shipping_cost DESC;

-- Warehouse-wise Orders
SELECT
    w.warehouse_name,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN warehouses w
ON o.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name
ORDER BY total_orders DESC;
-- =====================================================
-- SUPPLIER PERFORMANCE ANALYSIS
-- =====================================================

-- Total Sales by Supplier
SELECT
    s.supplier_name,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN suppliers s
ON o.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_sales DESC;

-- Total Profit by Supplier
SELECT
    s.supplier_name,
    SUM(o.profit) AS total_profit
FROM orders o
JOIN suppliers s
ON o.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_profit DESC;

-- Total Products Supplied
SELECT
    s.supplier_name,
    COUNT(DISTINCT o.product_id) AS total_products
FROM orders o
JOIN suppliers s
ON o.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_products DESC;

-- Supplier Sales by Country
SELECT
    s.country,
    SUM(o.sales) AS total_sales
FROM orders o
JOIN suppliers s
ON o.supplier_id = s.supplier_id
GROUP BY s.country
ORDER BY total_sales DESC;

-- Average Sales per Supplier
SELECT
    s.supplier_name,
    ROUND(AVG(o.sales), 2) AS average_sales
FROM orders o
JOIN suppliers s
ON o.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY average_sales DESC;
-- =====================================================
-- ADVANCED SQL QUERIES
-- =====================================================

-- Top 5 Customers by Sales using RANK()
SELECT
    c.customer_name,
    SUM(o.sales) AS total_sales,
    RANK() OVER (ORDER BY SUM(o.sales) DESC) AS sales_rank
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.customer_name;

--------------------------------------------------------

-- Top Products using DENSE_RANK()
SELECT
    p.product_name,
    SUM(o.sales) AS total_sales,
    DENSE_RANK() OVER (ORDER BY SUM(o.sales) DESC) AS product_rank
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name;

--------------------------------------------------------

-- Row Number for Orders
SELECT
    order_id,
    customer_id,
    sales,
    ROW_NUMBER() OVER (ORDER BY sales DESC) AS row_num
FROM orders;

--------------------------------------------------------

-- Categorize Orders using CASE
SELECT
    order_id,
    sales,
    CASE
        WHEN sales >= 10000 THEN 'High Sales'
        WHEN sales >= 5000 THEN 'Medium Sales'
        ELSE 'Low Sales'
    END AS sales_category
FROM orders;

--------------------------------------------------------

-- CTE: Top 10 Customers
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 10;

--------------------------------------------------------

-- Running Total of Sales
SELECT
    order_date,
    sales,
    SUM(sales) OVER (
        ORDER BY order_date
    ) AS running_total_sales
FROM orders;
