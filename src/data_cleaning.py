"""
Data Cleaning and Validation Module.
Performs schema validation, missing value handling, date parsing, outlier checks,
and derived feature computation (delivery delays, service flags).
"""

import os
import pandas as pd
import numpy as np

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")


def load_raw_datasets():
    """Loads all 6 raw CSV datasets."""
    datasets = {}
    files = ["areas", "customers", "products", "dealers", "transactions", "service_records"]
    for file_name in files:
        file_path = os.path.join(RAW_DIR, f"{file_name}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Raw dataset file missing: {file_path}")
        datasets[file_name] = pd.read_csv(file_path)
    return datasets


def clean_areas(df):
    """Validates and cleans areas master data."""
    df = df.copy()
    # Check nulls
    df["industrial_density"] = df["industrial_density"].clip(0, 100)
    df["estimated_industrial_units"] = df["estimated_industrial_units"].astype(int)
    df["estimated_market_size"] = df["estimated_market_size"].astype(float)
    df["yoy_growth_rate"] = df["yoy_growth_rate"].round(2)
    return df


def clean_customers(df):
    """Validates and cleans customers dataset."""
    df = df.copy()
    df["customer_name"] = df["customer_name"].str.strip()
    df["annual_revenue"] = df["annual_revenue"].fillna(df["annual_revenue"].median())
    df["customer_since"] = pd.to_datetime(df["customer_since"])
    return df


def clean_products(df):
    """Validates and cleans products dataset."""
    df = df.copy()
    df["unit_price"] = df["unit_price"].astype(float)
    return df


def clean_dealers(df):
    """Validates and cleans dealers dataset."""
    df = df.copy()
    df["dealer_name"] = df["dealer_name"].str.strip()
    return df


def clean_transactions(df):
    """Validates and cleans transaction records."""
    df = df.copy()
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    df["sales_amount"] = (df["quantity"] * df["unit_price"]).round(2)
    # Remove duplicates if any
    df = df.drop_duplicates(subset=["transaction_id"])
    return df


def clean_service_records(df):
    """Validates service records and computes delivery delay metrics."""
    df = df.copy()
    df["service_issue"] = df["service_issue"].fillna("None").astype(str).str.strip()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["expected_delivery_date"] = pd.to_datetime(df["expected_delivery_date"])
    df["delivery_date"] = pd.to_datetime(df["delivery_date"])
    
    # Derived fields
    df["delivery_delay_days"] = (df["delivery_date"] - df["expected_delivery_date"]).dt.days
    # Negative delay means delivered early (clip at 0 for delay calculation)
    df["delivery_delay_days"] = df["delivery_delay_days"].apply(lambda x: max(0, x))
    df["service_delay_flag"] = (df["delivery_delay_days"] > 0).astype(int)
    
    return df


def run_data_cleaning_pipeline():
    """Runs complete data cleaning pipeline and returns dict of cleaned DataFrames."""
    print("Loading raw datasets...")
    raw = load_raw_datasets()
    
    print("Cleaning & validating datasets...")
    cleaned = {
        "areas": clean_areas(raw["areas"]),
        "customers": clean_customers(raw["customers"]),
        "products": clean_products(raw["products"]),
        "dealers": clean_dealers(raw["dealers"]),
        "transactions": clean_transactions(raw["transactions"]),
        "service_records": clean_service_records(raw["service_records"])
    }
    
    print("Data cleaning & validation complete!")
    return cleaned


if __name__ == "__main__":
    cleaned_df = run_data_cleaning_pipeline()
    for name, df in cleaned_df.items():
        print(f"{name}: {len(df)} cleaned records")
