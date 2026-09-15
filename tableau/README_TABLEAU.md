# Tableau Workbook Setup & Implementation Guide

This document outlines the step-by-step instructions to create the **4-Dashboard Tableau Workbook (`regional_b2b_analytics.twbx`)** for the Regional B2B Market Penetration & Opportunity Scoring project.

---

## 1. Data Connection

1. Open **Tableau Desktop** or **Tableau Public**.
2. Connect to Data Source: Select **Text File** and browse to:
   `data/processed/dashboard_data.csv`
3. Verify fields & data types:
   - `taluka`: Text (Geographic Role -> County/District)
   - `latitude`: Number (decimal) -> Geographic Role -> Latitude
   - `longitude`: Number (decimal) -> Geographic Role -> Longitude
   - `opportunity_score`: Number (decimal)
   - `market_potential_score`: Number (decimal)
   - `current_penetration_rate`: Number (decimal)
   - `total_sales`: Number (decimal)
   - `primary_root_cause`: Text
   - `opportunity_category`: Text
   - `cluster_segment`: Text

---

## 2. Calculated Fields to Add in Tableau

| Calculated Field Name | Tableau Formula / Syntax | Description |
| :--- | :--- | :--- |
| **Penetration Gap %** | `100 - [current_penetration_rate]` | Untapped market potential percentage |
| **Opportunity Tier Code** | `IF [opportunity_score] >= 75 THEN "1. High" ELSEIF [opportunity_score] >= 50 THEN "2. Medium" ELSE "3. Low" END` | Sorting hierarchy for opportunity categories |
| **Sales per Customer** | `[total_sales] / [active_customers]` | Average customer account yield |
| **Service Delay Risk Flag** | `IF [avg_delivery_delay_days] > 2.0 THEN "High Delay Risk" ELSE "Normal Delivery" END` | Warning indicator for logistics bottlenecks |

---

## 3. Structure of the 4 Tableau Dashboards

### Dashboard 1 — Executive Overview
- **Header KPI Cards**:
  - Total Regional Sales (`SUM(total_sales)` formatted as Currency INR)
  - Active Customers (`SUM(active_customers)`)
  - Avg Market Penetration (`AVG(current_penetration_rate)` formatted as %)
  - High Opportunity Count (`COUNTD(IF opportunity_category = 'High Opportunity' THEN taluka END)`)
- **Visual 1**: Filled Map / Symbol Map of Pune Region colored by `opportunity_score` (Sequential Palette: Teal/Blue-Purple).
- **Visual 2**: Ranked Bar Chart of `total_sales` by `taluka`.
- **Filters**: District, Opportunity Category.

---

### Dashboard 2 — Market Penetration Matrix
- **Scatter Plot Visual**:
  - **X-axis**: `market_potential_score` (0 to 100)
  - **Y-axis**: `current_penetration_rate` (0% to 30%)
  - **Color**: `opportunity_category` (Green = High, Amber = Medium, Red = Low)
  - **Size**: `estimated_market_size`
  - **Label**: `taluka`
- **4-Quadrant Reference Lines**:
  - Constant Line on X-axis at 50.0 (Market Potential Median)
  - Constant Line on Y-axis at 15.0% (Regional Avg Penetration)
  - **Bottom-Right Quadrant Callout**: *HIGH OPPORTUNITY / UNTAPPED POTENTIAL (e.g. Ranjangaon, Shirur)*.

---

### Dashboard 3 — Opportunity Prioritization Ranking
- **Ranked Master Cross-Tab / Heatmap**:
  - Columns: Rank, Taluka, Opportunity Score, Market Potential, Penetration %, Penetration Gap %, YoY Growth %, Primary Root Cause, ML Cluster Segment.
  - Color Legend: Conditional formatting on `opportunity_score` (Green-Yellow-Red).
- **Interactive Action Filter**:
  - Clicking a row filters Dashboard 4 (Root Cause Analysis).

---

### Dashboard 4 — Root Cause Analysis & Business Recommendations
- **Single Area Drill-Down View**:
  - Selected Area Name Header Card
  - Dual-Axis Bar Chart: `avg_delivery_delay_days` vs `dealers_per_100_units`
  - Root Cause Summary Callout Box: `primary_root_cause` & `root_cause_details`
  - Strategic Action Recommendation Card: `recommended_action`

---

## 4. Tableau Workbook Export

Save the workbook as `regional_b2b_analytics.twbx` inside the `tableau/` folder of this repository.
