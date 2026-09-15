"""
Synthetic Data Generation Module for Regional B2B Market Penetration Project.
Simulates realistic industrial distributor sales, customer density, dealer network,
and service performance metrics across 13 major talukas/industrial areas in Pune region.
"""

import os
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# Set reproducible random seed
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")


def generate_areas():
    """Generates the master geographical areas dataset for Pune region."""
    areas_data = [
        {
            "area_id": "A001",
            "district": "Pune",
            "taluka": "Chakan",
            "area_name": "Chakan MIDC Phase 1-4",
            "latitude": 18.7602,
            "longitude": 73.8634,
            "industrial_density": 94,
            "midc_presence": 1,
            "estimated_industrial_units": 1450,
            "estimated_market_size": 125000000.0,
            "yoy_growth_rate": 14.2,
        },
        {
            "area_id": "A002",
            "district": "Pune",
            "taluka": "Talegaon",
            "area_name": "Talegaon Industrial Area",
            "latitude": 18.7304,
            "longitude": 73.6765,
            "industrial_density": 82,
            "midc_presence": 1,
            "estimated_industrial_units": 920,
            "estimated_market_size": 78000000.0,
            "yoy_growth_rate": 11.5,
        },
        {
            "area_id": "A003",
            "district": "Pune",
            "taluka": "Ranjangaon",
            "area_name": "Ranjangaon MIDC Industrial Hub",
            "latitude": 18.8471,
            "longitude": 74.2543,
            "industrial_density": 89,
            "midc_presence": 1,
            "estimated_industrial_units": 1180,
            "estimated_market_size": 110000000.0,
            "yoy_growth_rate": 15.8,
        },
        {
            "area_id": "A004",
            "district": "Pune",
            "taluka": "Pimpri-Chinchwad",
            "area_name": "PCPMC Auto Hub",
            "latitude": 18.6298,
            "longitude": 73.7997,
            "industrial_density": 98,
            "midc_presence": 1,
            "estimated_industrial_units": 1850,
            "estimated_market_size": 165000000.0,
            "yoy_growth_rate": 8.4,
        },
        {
            "area_id": "A005",
            "district": "Pune",
            "taluka": "Bhosari",
            "area_name": "Bhosari Industrial Estate",
            "latitude": 18.6385,
            "longitude": 73.8458,
            "industrial_density": 91,
            "midc_presence": 1,
            "estimated_industrial_units": 1320,
            "estimated_market_size": 105000000.0,
            "yoy_growth_rate": 7.6,
        },
        {
            "area_id": "A006",
            "district": "Pune",
            "taluka": "Shirur",
            "area_name": "Shirur Industrial Zone",
            "latitude": 18.8286,
            "longitude": 74.3789,
            "industrial_density": 76,
            "midc_presence": 1,
            "estimated_industrial_units": 850,
            "estimated_market_size": 65000000.0,
            "yoy_growth_rate": 13.1,
        },
        {
            "area_id": "A007",
            "district": "Pune",
            "taluka": "Baramati",
            "area_name": "Baramati High-Tech MIDC",
            "latitude": 18.1517,
            "longitude": 74.5772,
            "industrial_density": 68,
            "midc_presence": 1,
            "estimated_industrial_units": 650,
            "estimated_market_size": 52000000.0,
            "yoy_growth_rate": 9.2,
        },
        {
            "area_id": "A008",
            "district": "Pune",
            "taluka": "Daund",
            "area_name": "Daund Logistics & Industrial Belt",
            "latitude": 18.4651,
            "longitude": 74.5956,
            "industrial_density": 45,
            "midc_presence": 0,
            "estimated_industrial_units": 420,
            "estimated_market_size": 32000000.0,
            "yoy_growth_rate": 5.1,
        },
        {
            "area_id": "A009",
            "district": "Pune",
            "taluka": "Khed",
            "area_name": "Khed Auto Component Cluster",
            "latitude": 18.8504,
            "longitude": 73.9103,
            "industrial_density": 71,
            "midc_presence": 1,
            "estimated_industrial_units": 710,
            "estimated_market_size": 58000000.0,
            "yoy_growth_rate": 10.4,
        },
        {
            "area_id": "A010",
            "district": "Pune",
            "taluka": "Haveli",
            "area_name": "Haveli Engineering Belt",
            "latitude": 18.4412,
            "longitude": 73.8123,
            "industrial_density": 64,
            "midc_presence": 0,
            "estimated_industrial_units": 580,
            "estimated_market_size": 46000000.0,
            "yoy_growth_rate": 6.8,
        },
        {
            "area_id": "A011",
            "district": "Pune",
            "taluka": "Mulshi",
            "area_name": "Mulshi Light Manufacturing Zone",
            "latitude": 18.5912,
            "longitude": 73.6102,
            "industrial_density": 58,
            "midc_presence": 0,
            "estimated_industrial_units": 490,
            "estimated_market_size": 38000000.0,
            "yoy_growth_rate": 8.9,
        },
        {
            "area_id": "A012",
            "district": "Pune",
            "taluka": "Purandar",
            "area_name": "Purandar Agri & Industrial Park",
            "latitude": 18.2834,
            "longitude": 73.9741,
            "industrial_density": 50,
            "midc_presence": 0,
            "estimated_industrial_units": 390,
            "estimated_market_size": 29000000.0,
            "yoy_growth_rate": 6.2,
        },
        {
            "area_id": "A013",
            "district": "Pune",
            "taluka": "Maval",
            "area_name": "Maval Heavy Fabrication Corridor",
            "latitude": 18.7511,
            "longitude": 73.5412,
            "industrial_density": 75,
            "midc_presence": 1,
            "estimated_industrial_units": 780,
            "estimated_market_size": 62000000.0,
            "yoy_growth_rate": 9.8,
        },
    ]
    df = pd.DataFrame(areas_data)
    return df


def generate_products():
    """Generates product master table."""
    products_data = [
        {"product_id": "P001", "product_name": "3-Phase Induction Motor 10HP", "product_category": "Motors", "unit_price": 45000.0},
        {"product_id": "P002", "product_name": "Heavy Duty Taper Roller Bearing", "product_category": "Bearings", "unit_price": 6500.0},
        {"product_id": "P003", "product_name": "Modular Conveyor Belt Systems", "product_category": "Material Handling", "unit_price": 120000.0},
        {"product_id": "P004", "product_name": "High-Pressure Hydraulic Vane Pump", "product_category": "Hydraulics", "unit_price": 38000.0},
        {"product_id": "P005", "product_name": "Industrial Photoelectric Sensor Kit", "product_category": "Automation", "unit_price": 12500.0},
        {"product_id": "P006", "product_name": "CNC Milling Carbide Tool Inserts (Pack)", "product_category": "Metal Cutting", "unit_price": 18500.0},
        {"product_id": "P007", "product_name": "Programmable Logic Controller (PLC)", "product_category": "Automation", "unit_price": 85000.0},
        {"product_id": "P008", "product_name": "Industrial Variable Frequency Drive 15kW", "product_category": "Electricals", "unit_price": 54000.0},
        {"product_id": "P009", "product_name": "High-Tensile Steel Fastener Assortment", "product_category": "Fasteners", "unit_price": 8500.0},
        {"product_id": "P010", "product_name": "Pneumatic Double-Acting Cylinder", "product_category": "Hydraulics", "unit_price": 22000.0},
        {"product_id": "P011", "product_name": "Automated Lubrication System", "product_category": "Material Handling", "unit_price": 42000.0},
        {"product_id": "P012", "product_name": "Precision Ball Screw Assembly", "product_category": "Bearings", "unit_price": 31000.0},
        {"product_id": "P013", "product_name": "Heavy Duty Helical Gearbox", "product_category": "Motors", "unit_price": 95000.0},
        {"product_id": "P014", "product_name": "Industrial Safety Light Curtain", "product_category": "Safety Gear", "unit_price": 28000.0},
        {"product_id": "P015", "product_name": "High Temperature Heat Exchanger Valve", "product_category": "Hydraulics", "unit_price": 49000.0},
    ]
    return pd.DataFrame(products_data)


def generate_dealers(areas_df):
    """Generates dealers table. Simulates lower dealer presence in Ranjangaon and Shirur."""
    dealer_names_prefix = [
        "Apex", "Western", "Deccan", "Pune Premier", "Maharashtra", "Sahyadri",
        "Techno", "Precision", "Industrial Hub", "Synergy", "Maratha", "Vanguard",
        "Metro", "Standard", "Everest", "Global", "United", "Zenith"
    ]
    dealer_types = ["Authorized Master", "Regional Distributor", "Direct Dealer"]
    capacities = ["High", "Medium", "Low"]
    
    dealers = []
    d_count = 1
    
    for _, area in areas_df.iterrows():
        area_id = area["area_id"]
        taluka = area["taluka"]
        
        # Determine number of dealers based on business logic
        if taluka in ["Pimpri-Chinchwad", "Chakan", "Bhosari"]:
            num_dealers = random.randint(5, 7)
        elif taluka in ["Talegaon", "Khed", "Maval"]:
            num_dealers = random.randint(3, 4)
        elif taluka in ["Ranjangaon", "Shirur"]:
            # Intentionally few dealers to simulate Distribution Gap
            num_dealers = 1
        else:
            num_dealers = random.randint(1, 2)
            
        for _ in range(num_dealers):
            prefix = random.choice(dealer_names_prefix)
            d_id = f"D{d_count:03d}"
            capacity = "Low" if taluka in ["Ranjangaon", "Shirur"] else random.choice(capacities)
            dealer_type = "Direct Dealer" if taluka in ["Ranjangaon", "Shirur"] else random.choice(dealer_types)
            
            dealers.append({
                "dealer_id": d_id,
                "dealer_name": f"{prefix} Industrial Solutions ({taluka})",
                "area_id": area_id,
                "dealer_type": dealer_type,
                "capacity": capacity,
                "active_status": "Active" if random.random() > 0.1 else "Inactive"
            })
            d_count += 1
            
    return pd.DataFrame(dealers)


def generate_customers(areas_df):
    """Generates ~750 realistic B2B customers with target active customer counts per area."""
    company_prefixes = [
        "Bharat", "Precision", "Synergy", "Apex", "Matrix", "Kirloskar-Style",
        "Force", "Tata-Partner", "Deccan", "Mahindra-Tier1", "Western", "Sigma",
        "Dynamic", "TechnoCraft", "Vanguard", "Omni", "Pragati", "Sai", "Shree",
        "Kalyani", "Thermax-Vendor", "Atlas", "Schneider-Supplier", "Siemens-Tier2"
    ]
    company_suffixes = [
        "Engineering Pvt Ltd", "Auto Components", "Tools & Dies", "Forgings & Castings",
        "Fabricators", "Automation Systems", "Polymers", "Tech Solutions",
        "Industries", "Metal Works", "Chemicals & Processing", "Packaging Solutions"
    ]
    industries = [
        "Automotive", "Engineering", "Metal Fabrication", "Chemicals",
        "Pharmaceuticals", "Packaging", "Food Processing", "Electronics", "Textile"
    ]
    company_sizes = ["Small", "Medium", "Large", "Enterprise"]
    
    # Target active customers per area (reflecting Penetration Rate)
    # Chakan, PCMC, Bhosari -> High penetration (~20-25% of estimated units)
    # Ranjangaon, Shirur -> Low penetration (~6-9% of estimated units despite huge potential)
    penetration_targets = {
        "A001": 310,  # Chakan (~21%)
        "A002": 150,  # Talegaon (~16%)
        "A003": 85,   # Ranjangaon (~7.2% -> Untapped!)
        "A004": 420,  # PCMC (~22.7%)
        "A005": 280,  # Bhosari (~21.2%)
        "A006": 65,   # Shirur (~7.6% -> Untapped!)
        "A007": 110,  # Baramati (~16.9%)
        "A008": 55,   # Daund (~13.1%)
        "A009": 115,  # Khed (~16.2%)
        "A010": 80,   # Haveli (~13.8%)
        "A011": 60,   # Mulshi (~12.2%)
        "A012": 45,   # Purandar (~11.5%)
        "A013": 125,  # Maval (~16.0%)
    }
    
    customers = []
    c_count = 1
    
    for area_id, count in penetration_targets.items():
        for _ in range(count):
            c_id = f"C{c_count:04d}"
            name = f"{random.choice(company_prefixes)} {random.choice(company_suffixes)}"
            industry = random.choice(industries)
            size = random.choice(company_sizes)
            rev_base = {"Small": 15e6, "Medium": 50e6, "Large": 150e6, "Enterprise": 500e6}[size]
            revenue = round(rev_base * random.uniform(0.6, 1.8), -5)
            since_year = random.randint(2018, 2024)
            since_date = f"{since_year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            
            customers.append({
                "customer_id": c_id,
                "customer_name": name,
                "area_id": area_id,
                "industry_type": industry,
                "company_size": size,
                "annual_revenue": revenue,
                "customer_status": "Active",
                "customer_since": since_date
            })
            c_count += 1
            
    return pd.DataFrame(customers)


def generate_transactions_and_services(customers_df, products_df, dealers_df, total_transactions=8500):
    """Generates 8,500 realistic B2B transactions and corresponding service tracking records."""
    dealers_by_area = dealers_df.groupby("area_id")["dealer_id"].apply(list).to_dict()
    
    transactions = []
    service_records = []
    
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 8, 31)
    date_range_days = (end_date - start_date).days
    
    # Customer weights (higher revenue customers buy more frequently)
    cust_weights = customers_df["annual_revenue"].values
    cust_weights = cust_weights / cust_weights.sum()
    
    products_list = products_df.to_dict("records")
    
    for t_idx in range(1, total_transactions + 1):
        t_id = f"T{t_idx:06d}"
        
        # Pick customer weighted by revenue
        cust_row = customers_df.iloc[np.random.choice(len(customers_df), p=cust_weights)]
        c_id = cust_row["customer_id"]
        area_id = cust_row["area_id"]
        
        # Select product
        prod = random.choice(products_list)
        p_id = prod["product_id"]
        base_price = prod["unit_price"]
        
        # Pick dealer servicing this area
        available_dealers = dealers_by_area.get(area_id, dealers_df["dealer_id"].tolist())
        d_id = random.choice(available_dealers)
        
        # Transaction date
        random_days = random.randint(0, date_range_days)
        tx_date = start_date + timedelta(days=random_days)
        tx_date_str = tx_date.strftime("%Y-%m-%d")
        
        # Quantity & Pricing
        quantity = random.randint(1, 15)
        # Apply bulk discount for larger orders
        discount_factor = 0.95 if quantity >= 10 else 1.0
        unit_price = round(base_price * discount_factor, 2)
        sales_amount = round(quantity * unit_price, 2)
        
        transactions.append({
            "transaction_id": t_id,
            "customer_id": c_id,
            "product_id": p_id,
            "dealer_id": d_id,
            "area_id": area_id,
            "transaction_date": tx_date_str,
            "quantity": quantity,
            "unit_price": unit_price,
            "sales_amount": sales_amount
        })
        
        # Generate Service Record linked 1-to-1
        s_id = f"S{t_idx:06d}"
        expected_days = random.randint(1, 3)
        expected_delivery = tx_date + timedelta(days=expected_days)
        
        # Delivery Delay logic based on area and dealer capacity
        # Ranjangaon (A003) & Shirur (A006) experience high delivery delays due to warehouse bottleneck
        if area_id in ["A003", "A006"]:
            actual_delay = random.choices([0, 1, 3, 5, 8], weights=[0.1, 0.2, 0.3, 0.25, 0.15])[0]
            response_time_hrs = random.randint(36, 96)
            issues_pool = ["Dealer Stockout", "Transport Routing Delay", "Warehouse Delay", "Parts Damage", "None"]
            issue_weights = [0.35, 0.30, 0.20, 0.05, 0.10]
        elif area_id in ["A001", "A004", "A005"]:
            actual_delay = random.choices([0, 1, 2], weights=[0.8, 0.15, 0.05])[0]
            response_time_hrs = random.randint(4, 18)
            issues_pool = ["None", "Minor Transport Delay"]
            issue_weights = [0.92, 0.08]
        else:
            actual_delay = random.choices([0, 1, 2, 4], weights=[0.5, 0.3, 0.15, 0.05])[0]
            response_time_hrs = random.randint(12, 36)
            issues_pool = ["None", "Stock Delay", "Transport Delay"]
            issue_weights = [0.75, 0.15, 0.10]
            
        actual_delivery = expected_delivery + timedelta(days=actual_delay)
        issue = random.choices(issues_pool, weights=issue_weights)[0]
        
        service_records.append({
            "service_id": s_id,
            "transaction_id": t_id,
            "dealer_id": d_id,
            "area_id": area_id,
            "order_date": tx_date_str,
            "expected_delivery_date": expected_delivery.strftime("%Y-%m-%d"),
            "delivery_date": actual_delivery.strftime("%Y-%m-%d"),
            "response_time_hours": response_time_hrs,
            "service_issue": issue
        })
        
    return pd.DataFrame(transactions), pd.DataFrame(service_records)


def main():
    """Generates all CSV datasets and writes to data/raw/."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating synthetic datasets for B2B Pune Market Analysis...")

    areas_df = generate_areas()
    products_df = generate_products()
    dealers_df = generate_dealers(areas_df)
    customers_df = generate_customers(areas_df)
    transactions_df, service_df = generate_transactions_and_services(
        customers_df, products_df, dealers_df, total_transactions=8500
    )

    areas_df.to_csv(os.path.join(OUTPUT_DIR, "areas.csv"), index=False)
    products_df.to_csv(os.path.join(OUTPUT_DIR, "products.csv"), index=False)
    dealers_df.to_csv(os.path.join(OUTPUT_DIR, "dealers.csv"), index=False)
    customers_df.to_csv(os.path.join(OUTPUT_DIR, "customers.csv"), index=False)
    transactions_df.to_csv(os.path.join(OUTPUT_DIR, "transactions.csv"), index=False)
    service_df.to_csv(os.path.join(OUTPUT_DIR, "service_records.csv"), index=False)

    print(f"Data generation complete!")
    print(f"Areas: {len(areas_df)} records")
    print(f"Products: {len(products_df)} records")
    print(f"Dealers: {len(dealers_df)} records")
    print(f"Customers: {len(customers_df)} records")
    print(f"Transactions: {len(transactions_df)} records")
    print(f"Service Records: {len(service_df)} records")


if __name__ == "__main__":
    main()
