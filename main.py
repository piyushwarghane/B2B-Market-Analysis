"""
Master Execution Pipeline for Regional B2B Market Penetration & Sales Analytics.

Executes end-to-end data workflow:
Raw Data Generation -> Cleaning & Validation -> SQL DB Ingestion -> Aggregations ->
Opportunity Scoring -> Root Cause Diagnosis -> K-Means ML Clustering -> Dashboard Export.
"""

import os
import sys
import pandas as pd

# Add project root to Python path
sys.path.append(os.path.dirname(__file__))

from src.data_generation import main as run_data_generation
from src.data_cleaning import run_data_cleaning_pipeline
from src.feature_engineering import run_feature_engineering_pipeline
from src.opportunity_model import compute_opportunity_scoring
from src.root_cause import evaluate_root_causes
from src.clustering import run_kmeans_clustering

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "data", "processed")


def main():
    print("=" * 80)
    print("B2B MARKET PENETRATION & OPPORTUNITY SCORING ANALYTICS PIPELINE")
    print("Geographic Scope: Pune Region Industrial Belt (Maharashtra)")
    print("=" * 80)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # 1. Raw Data Generation
    print("\n[PHASE 1] Synthetic Data Generation...")
    run_data_generation()

    # 2. Feature Engineering & Database Ingestion
    print("\n[PHASE 2 & 3] Data Cleaning & SQL Database Ingestion...")
    area_metrics_df = run_feature_engineering_pipeline()
    area_metrics_df.to_csv(os.path.join(PROCESSED_DIR, "area_metrics.csv"), index=False)

    # 3. Opportunity Scoring Model
    print("\n[PHASE 4] Market Potential & Opportunity Scoring Model...")
    scored_df = compute_opportunity_scoring(area_metrics_df)
    scored_df.to_csv(os.path.join(PROCESSED_DIR, "opportunity_scores.csv"), index=False)

    # 4. Root Cause Analysis Model
    print("\n[PHASE 5] Multi-Vector Root Cause Diagnostics...")
    root_cause_df = evaluate_root_causes(scored_df)
    root_cause_df.to_csv(os.path.join(PROCESSED_DIR, "root_cause_summary.csv"), index=False)

    # 5. Scikit-Learn K-Means Clustering
    print("\n[PHASE 6] Scikit-Learn K-Means Unsupervised Segmentation...")
    final_df, kmeans_model, scaler = run_kmeans_clustering(root_cause_df)
    final_df.to_csv(os.path.join(PROCESSED_DIR, "cluster_segments.csv"), index=False)

    # 6. Consolidated Dashboard Data Export
    print("\n[PHASE 7] Exporting Consolidated Dashboard Dataset...")
    dashboard_path = os.path.join(PROCESSED_DIR, "dashboard_data.csv")
    final_df.to_csv(dashboard_path, index=False)

    print(f"Master dashboard export created at: {dashboard_path}")

    # Display Executive Summary
    print("\n" + "=" * 80)
    print("FINAL AREA OPPORTUNITY RANKING & ROOT CAUSE SUMMARY")
    print("=" * 80)
    summary_cols = [
        "opportunity_rank", "taluka", "opportunity_score", "opportunity_category",
        "market_potential_score", "current_penetration_rate", "primary_root_cause",
        "cluster_segment"
    ]
    print(final_df[summary_cols].to_string(index=False))
    print("=" * 80)
    print("Pipeline Execution Complete Successfully!\n")


if __name__ == "__main__":
    main()
