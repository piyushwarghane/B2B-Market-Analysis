"""
Feature Engineering and Database Pipeline.
Loads cleaned data into SQLite database (database/b2b_analytics.db), runs SQL queries,
and computes aggregated metrics per area for opportunity scoring and root-cause modeling.
"""

import os
import sqlite3
import pandas as pd
from src.data_cleaning import run_data_cleaning_pipeline

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "b2b_analytics.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "schema.sql")


def initialize_database(cleaned_data):
    """Creates SQLite database, executes schema.sql, and inserts cleaned DataFrames."""
    # Ensure database dir exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except Exception:
            pass
    
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    cursor = conn.cursor()
    
    # Read schema
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    
    cursor.executescript(schema_sql)
    conn.commit()
    
    # Insert tables
    print("Populating SQLite database tables...")
    cleaned_data["areas"].to_sql("areas", conn, if_exists="append", index=False)
    cleaned_data["customers"].to_sql("customers", conn, if_exists="append", index=False, chunksize=1000)
    cleaned_data["products"].to_sql("products", conn, if_exists="append", index=False)
    cleaned_data["dealers"].to_sql("dealers", conn, if_exists="append", index=False)
    cleaned_data["transactions"].to_sql("transactions", conn, if_exists="append", index=False, chunksize=2000)
    cleaned_data["service_records"].to_sql("service_records", conn, if_exists="append", index=False, chunksize=2000)
    
    conn.commit()
    print("Database initialization & loading complete.")
    return conn


def extract_area_features(conn):
    """Executes optimized CTE SQL aggregations to extract unified area metrics."""
    query = """
    WITH tx_agg AS (
        SELECT 
            area_id, 
            SUM(sales_amount) AS total_sales,
            COUNT(transaction_id) AS total_transactions,
            AVG(sales_amount) AS avg_order_value
        FROM transactions 
        GROUP BY area_id
    ),
    cust_agg AS (
        SELECT 
            area_id, 
            COUNT(customer_id) AS active_customers
        FROM customers 
        GROUP BY area_id
    ),
    dealer_agg AS (
        SELECT 
            area_id, 
            COUNT(dealer_id) AS dealer_count
        FROM dealers 
        WHERE active_status = 'Active' 
        GROUP BY area_id
    ),
    service_agg AS (
        SELECT 
            area_id, 
            AVG(delivery_delay_days) AS avg_delivery_delay_days,
            AVG(response_time_hours) AS avg_response_time_hours,
            ROUND((SUM(service_delay_flag) * 100.0 / COUNT(service_id)), 2) AS service_delay_pct
        FROM service_records 
        GROUP BY area_id
    )
    SELECT 
        a.area_id,
        a.district,
        a.taluka,
        a.area_name,
        a.latitude,
        a.longitude,
        a.industrial_density,
        a.midc_presence,
        a.estimated_industrial_units,
        a.estimated_market_size,
        a.yoy_growth_rate,
        
        COALESCE(t.total_sales, 0.0) AS total_sales,
        COALESCE(t.total_transactions, 0) AS total_transactions,
        COALESCE(t.avg_order_value, 0.0) AS avg_order_value,
        
        COALESCE(c.active_customers, 0) AS active_customers,
        ROUND((COALESCE(c.active_customers, 0) * 100.0 / a.estimated_industrial_units), 2) AS current_penetration_rate,
        ROUND(100.0 - (COALESCE(c.active_customers, 0) * 100.0 / a.estimated_industrial_units), 2) AS penetration_gap,
        
        COALESCE(d.dealer_count, 0) AS dealer_count,
        ROUND((COALESCE(d.dealer_count, 0) * 100.0 / a.estimated_industrial_units), 2) AS dealers_per_100_units,
        
        COALESCE(s.avg_delivery_delay_days, 0.0) AS avg_delivery_delay_days,
        COALESCE(s.avg_response_time_hours, 0.0) AS avg_response_time_hours,
        COALESCE(s.service_delay_pct, 0.0) AS service_delay_pct

    FROM areas a
    LEFT JOIN tx_agg t ON a.area_id = t.area_id
    LEFT JOIN cust_agg c ON a.area_id = c.area_id
    LEFT JOIN dealer_agg d ON a.area_id = d.area_id
    LEFT JOIN service_agg s ON a.area_id = s.area_id
    ORDER BY total_sales DESC;
    """
    
    area_metrics_df = pd.read_sql_query(query, conn)
    return area_metrics_df


def run_feature_engineering_pipeline():
    """Runs data cleaning, initializes DB, and extracts area features."""
    cleaned_data = run_data_cleaning_pipeline()
    conn = initialize_database(cleaned_data)
    area_features_df = extract_area_features(conn)
    conn.close()
    return area_features_df


if __name__ == "__main__":
    df = run_feature_engineering_pipeline()
    print("Extracted Area Features:")
    print(df[["taluka", "total_sales", "active_customers", "current_penetration_rate", "avg_delivery_delay_days"]].to_string())
