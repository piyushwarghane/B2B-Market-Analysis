# Regional B2B Market Penetration & Opportunity Scoring Analytics

An end-to-end data analytics and market intelligence project for an industrial distributor operating across the **Pune region of Maharashtra, India**. 

The system processes simulated B2B transactions, customer master tables, dealer networks, and service delivery performance logs to quantify **Market Potential**, compute composite **Opportunity Scores**, diagnose **Root Causes of Underperformance**, and deliver interactive executive dashboards.

---

## 📌 Business Objective

> **“For an industrial distributor in the Pune region, which districts/talukas have the greatest untapped sales potential, and why are underperforming areas failing?”**

This project identifies high-potential, low-penetration industrial hubs (e.g. **Ranjangaon MIDC**, **Shirur**, **Chakan**) and distinguishes whether underperformance is driven by a **Demand Gap**, a **Distribution Gap**, or a **Service Gap**.

---

## 🛠 Tech Stack

- **Data Processing & ETL**: Python 3, Pandas, NumPy
- **Database & Querying**: SQL, SQLite (`database/b2b_analytics.db`), SQL CTE Aggregations
- **Machine Learning**: Scikit-Learn (K-Means Clustering, StandardScaler)
- **Visual Dashboards**:
  - **Interactive Web Dashboard**: HTML5, CSS3 (Glassmorphic Dark Theme), JavaScript, Chart.js (`dashboard/index.html`)
  - **Tableau Desktop / Public**: Workbook Specification & Guide (`tableau/README_TABLEAU.md`)
- **Documentation**: Markdown, Mermaid ER Diagrams, Technical Reports (`reports/`)

---

## 🏗 Overall Architecture

```text
 ┌────────────────────────────────────────────────────────┐
 │                    Simulated Data                      │
 │  Areas (13) | Customers (1.9k) | Products (15)         │
 │  Dealers (41) | Transactions (8.5k) | Service Logs     │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │                Data Cleaning & Validation              │
 │               (`src/data_cleaning.py`)                 │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │              SQLite Database & CTE SQL Engine          │
 │        (`database/schema.sql`, `src/feature_eng.py`)   │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │               Opportunity Scoring Model                │
 │             (`src/opportunity_model.py`)               │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │           Multi-Vector Root Cause Engine               │
 │                (`src/root_cause.py`)                   │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │            Scikit-Learn K-Means Clustering             │
 │                (`src/clustering.py`)                   │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │          Tableau / Interactive Web Dashboard           │
 │       (`dashboard/index.html` & `dashboard_data.csv`)  │
 └────────────────────────────────────────────────────────┘
```

---

## 📂 Project Directory Structure

```text
b2b_market_analysis/
│
├── data/
│   ├── raw/
│   │   ├── areas.csv
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── dealers.csv
│   │   ├── transactions.csv
│   │   └── service_records.csv
│   └── processed/
│       ├── area_metrics.csv
│       ├── opportunity_scores.csv
│       ├── root_cause_summary.csv
│       ├── cluster_segments.csv
│       └── dashboard_data.csv
│
├── database/
│   ├── schema.sql
│   ├── analysis_queries.sql
│   └── b2b_analytics.db
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_market_penetration.ipynb
│   ├── 03_opportunity_scoring.ipynb
│   └── 04_root_cause_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_generation.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── market_analysis.py
│   ├── opportunity_model.py
│   ├── root_cause.py
│   └── clustering.py
│
├── dashboard/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── tableau/
│   ├── README_TABLEAU.md
│   └── workbook_spec.json
│
├── reports/
│   ├── business_recommendations.md
│   ├── time_reduction_analysis.md
│   └── project_documentation.md
│
├── requirements.txt
├── README.md
└── main.py
```

---

## 📊 Final Area Opportunity Ranking (Pune Region)

| Rank | Taluka | Opportunity Score | Category | Market Potential | Current Penetration | Primary Root Cause | Recommended Action |
| ---: | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **1** | **Chakan** | **86.1** | High Opportunity | 85.4 | 21.4% | Distribution Gap | Expand authorized dealer network & onboard tier-1 distributors. |
| **2** | **Ranjangaon** | **77.0** | High Opportunity | 80.2 | **7.2%** | **Service Gap** | Establish local micro-warehouse in MIDC to solve 4.2-day delay. |
| **3** | **Pimpri-Chinchwad**| **71.1** | Medium Opportunity| 89.6 | 22.7% | Distribution Gap | Optimize key enterprise retention & cross-sell automation kits. |
| **4** | **Talegaon** | **68.6** | Medium Opportunity| 62.6 | 16.3% | Service Gap | Improve delivery fleet routing from Chakan hub. |
| **5** | **Bhosari** | **62.2** | Medium Opportunity| 69.9 | 21.2% | Service Gap | Maintain dealer incentive program & upsell high-margin lines. |
| **6** | **Shirur** | **61.4** | Medium Opportunity| 58.5 | **7.7%** | **Service Gap** | Partner with regional logistics provider for daily shuttles. |
| **7** | **Khed** | **61.0** | Medium Opportunity| 49.7 | 16.2% | Service Gap | Target auto component units with bulk pricing contracts. |
| **8** | **Maval** | **60.4** | Medium Opportunity| 52.3 | 16.0% | Service Gap | Expand product range to heavy fabrication units. |
| **9** | **Baramati** | **56.0** | Medium Opportunity| 44.8 | 16.9% | Service Gap | Focus sales outreach on agro-processing & textile machinery. |
| **10**| **Mulshi** | **45.6** | Low Opportunity | 15.0 | 12.2% | Demand Gap | Adopt key-account sales strategy rather than network expansion. |
| **11**| **Haveli** | **40.2** | Low Opportunity | 17.6 | 13.8% | Service Gap | Maintain existing channel coverage without capital expansion. |
| **12**| **Purandar** | **34.6** | Low Opportunity | 4.4 | 11.5% | Demand Gap | Serve via remote catalog orders and 3rd-party shipping. |
| **13**| **Daund** | **29.8** | Low Opportunity | 0.8 | 13.1% | Demand Gap | Low macro demand density; maintain minimal direct sales. |

---

## ⚡ Quickstart Execution Guide

### 1. Installation
Clone the repository and install required dependencies:
```bash
git clone https://github.com/your-username/b2b-market-analysis.git
cd b2b-market-analysis
pip install -r requirements.txt
```

### 2. Run the Full Analytics Pipeline
Execute `main.py` to run the end-to-end workflow:
```bash
python main.py
```
This automatically runs data generation, cleaning, SQLite ingestion, SQL aggregations, opportunity scoring, root-cause diagnostics, K-Means clustering, and exports clean datasets into `data/processed/dashboard_data.csv`.

### 3. Open the Interactive Web Dashboard
Simply double-click `dashboard/index.html` or open it in any web browser to view the interactive matrix chart, opportunity ranking table, and area drill-down cards.

---

## 🎯 Resume Description Bullet Points

Use these verified bullet points on your resume:

- **Built an End-to-End B2B Regional Market Analytics Pipeline**: Analyzed 8,500+ simulated industrial transactions across 13 talukas in the Pune region using **Python, SQL (SQLite), Pandas, Scikit-learn, and Tableau**.
- **Engineered Opportunity Scoring & Root-Cause Models**: Formulated a multi-factor Opportunity Score (0–100) combining Market Potential, YoY Growth, Penetration Gap, and Service SLA metrics; automated diagnostic classification tagging **Demand Gaps, Distribution Gaps, and Service Gaps**.
- **Segmented Markets with Scikit-learn K-Means**: Applied $K$-Means clustering to segment industrial areas into 4 distinct commercial profiles, identifying **Ranjangaon MIDC** as a prime untapped market (7.2% penetration vs 80.2 potential score).
- **Reduced Analysis Cycle Time by ~93.3%**: Replaced legacy manual Excel report preparation (2.5 hours) with an automated SQL/Python ETL pipeline and interactive visual dashboard (10 minutes).
