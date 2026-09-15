"""
Scikit-learn K-Means Area Clustering Module.
Uses unsupervised machine learning to segment industrial areas in Pune region
based on market, sales, penetration, and service logistics features.
Compares ML cluster assignments with heuristic Opportunity Scores.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def run_kmeans_clustering(root_cause_df, n_clusters=4, random_state=42):
    """
    Applies StandardScaler and KMeans clustering to segment areas into 4 business profiles:
    - High Untapped Opportunity
    - Mature Market Leaders
    - Emerging Growth Markets
    - Low Potential / Niche Markets
    """
    df = root_cause_df.copy()

    # Features selected for ML segmentation
    feature_cols = [
        "industrial_density",
        "estimated_market_size",
        "total_sales",
        "yoy_growth_rate",
        "current_penetration_rate",
        "dealers_per_100_units",
        "avg_delivery_delay_days"
    ]

    X = df[feature_cols].values

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)

    df["cluster_id"] = cluster_labels

    # Interpret clusters by inspecting mean values per cluster
    cluster_summary = df.groupby("cluster_id").agg({
        "total_sales": "mean",
        "current_penetration_rate": "mean",
        "market_potential_score": "mean",
        "opportunity_score": "mean",
        "avg_delivery_delay_days": "mean"
    }).reset_index()

    # Map cluster IDs to business label names based on opportunity & penetration characteristics
    # Cluster with highest opportunity score & low penetration -> High Untapped Opportunity
    # Cluster with highest total sales & high penetration -> Mature Market Leaders
    cluster_name_map = {}
    for cid in range(n_clusters):
        c_rows = df[df["cluster_id"] == cid]
        avg_opp = c_rows["opportunity_score"].mean()
        avg_pen = c_rows["current_penetration_rate"].mean()
        avg_sales = c_rows["total_sales"].mean()

        if avg_opp >= 75.0 and avg_pen < 35.0:
            name = "Cluster 1: High Untapped Opportunity"
        elif avg_pen >= 50.0 or avg_sales > 100e6:
            name = "Cluster 0: Mature Market Leaders"
        elif avg_opp >= 55.0:
            name = "Cluster 2: Emerging Growth Markets"
        else:
            name = "Cluster 3: Low Potential / Niche Markets"
            
        cluster_name_map[cid] = name

    df["cluster_segment"] = df["cluster_id"].map(cluster_name_map)

    print("K-Means Clustering complete across 13 Pune industrial areas.")
    return df, kmeans, scaler


if __name__ == "__main__":
    from src.feature_engineering import run_feature_engineering_pipeline
    from src.opportunity_model import compute_opportunity_scoring
    from src.root_cause import evaluate_root_causes

    area_metrics = run_feature_engineering_pipeline()
    scored_df = compute_opportunity_scoring(area_metrics)
    rc_df = evaluate_root_causes(scored_df)
    clustered_df, _, _ = run_kmeans_clustering(rc_df)

    print("\nML Clustering vs Opportunity Score Alignment:")
    print(clustered_df[[
        "taluka", "opportunity_score", "opportunity_category", "cluster_id", "cluster_segment"
    ]].to_string())
