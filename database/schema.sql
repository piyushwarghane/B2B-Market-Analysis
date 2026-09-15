-- B2B Pune Market Penetration & Sales Analytics Schema
-- Relational Database Definition with Foreign Keys & Indexes

DROP TABLE IF EXISTS service_records;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS dealers;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS areas;

-- 1. Geographical Master Table
CREATE TABLE areas (
    area_id VARCHAR(10) PRIMARY KEY,
    district VARCHAR(50) NOT NULL,
    taluka VARCHAR(50) NOT NULL,
    area_name VARCHAR(100) NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    industrial_density INTEGER NOT NULL,
    midc_presence INTEGER NOT NULL,
    estimated_industrial_units INTEGER NOT NULL,
    estimated_market_size REAL NOT NULL,
    yoy_growth_rate REAL NOT NULL
);

-- 2. Customer Master Table
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    area_id VARCHAR(10) NOT NULL,
    industry_type VARCHAR(50) NOT NULL,
    company_size VARCHAR(20) NOT NULL,
    annual_revenue REAL NOT NULL,
    customer_status VARCHAR(20) NOT NULL,
    customer_since DATE NOT NULL,
    FOREIGN KEY (area_id) REFERENCES areas(area_id)
);

-- 3. Product Master Table
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    unit_price REAL NOT NULL
);

-- 4. Dealer Master Table
CREATE TABLE dealers (
    dealer_id VARCHAR(10) PRIMARY KEY,
    dealer_name VARCHAR(100) NOT NULL,
    area_id VARCHAR(10) NOT NULL,
    dealer_type VARCHAR(50) NOT NULL,
    capacity VARCHAR(20) NOT NULL,
    active_status VARCHAR(20) NOT NULL,
    FOREIGN KEY (area_id) REFERENCES areas(area_id)
);

-- 5. Sales Transactions Table
CREATE TABLE transactions (
    transaction_id VARCHAR(12) PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    dealer_id VARCHAR(10) NOT NULL,
    area_id VARCHAR(10) NOT NULL,
    transaction_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    sales_amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (dealer_id) REFERENCES dealers(dealer_id),
    FOREIGN KEY (area_id) REFERENCES areas(area_id)
);

-- 6. Service & Delivery Performance Table
CREATE TABLE service_records (
    service_id VARCHAR(12) PRIMARY KEY,
    transaction_id VARCHAR(12) NOT NULL,
    dealer_id VARCHAR(10) NOT NULL,
    area_id VARCHAR(10) NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    response_time_hours INTEGER NOT NULL,
    service_issue VARCHAR(100) NOT NULL,
    delivery_delay_days INTEGER DEFAULT 0,
    service_delay_flag INTEGER DEFAULT 0,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (dealer_id) REFERENCES dealers(dealer_id),
    FOREIGN KEY (area_id) REFERENCES areas(area_id)
);

-- Performance Indexes
CREATE INDEX idx_tx_area ON transactions(area_id);
CREATE INDEX idx_tx_customer ON transactions(customer_id);
CREATE INDEX idx_tx_date ON transactions(transaction_date);
CREATE INDEX idx_srv_area ON service_records(area_id);
CREATE INDEX idx_dealers_area ON dealers(area_id);
