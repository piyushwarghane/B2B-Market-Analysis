"""
Market Penetration and Opportunity Scoring Model Module.
Calculates normalized Market Potential Score, Service Performance Score,
Penetration Gap, and final composite Opportunity Score (0-100 scale).
Ranks areas and classifies them into High, Medium, or Low Opportunity tiers.
"""

import pandas as pd
import numpy as np


def min_max_normalize(series):
    """Normalizes a numeric series to 0-100 scale."""
    min_val = series.min()
    max_val = series.max()
    if max_val == min_val:
        return pd.Series(100.0, index=series.index)
    return ((series - min_val) / (max_val - min_val)) * 100.0


def calculate_market_potential_score(df):
    """
    Computes Market Potential Score (0-100) using:
    - 30% Industrial Density
    - 25% Estimated Market Size
    - 20% MIDC Presence (100 or 0)
    - 15% Industrial Growth Rate
    - 10% Customer Density (estimated units normalized)
    """
    ind_density_norm = min_max_normalize(df["industrial_density"])
    mkt_size_norm = min_max_normalize(df["estimated_market_size"])
    midc_score = df["midc_presence"].apply(lambda x: 100.0 if x == 1 else 0.0)
    growth_norm = min_max_normalize(df["yoy_growth_rate"])
    cust_density_norm = min_max_normalize(df["estimated_industrial_units"])

    market_potential_score = (
        0.30 * ind_density_norm +
        0.25 * mkt_size_norm +
        0.20 * midc_score +
        0.15 * growth_norm +
        0.10 * cust_density_norm
    )
    return market_potential_score.round(2), growth_norm


def calculate_service_performance_score(df):
    """
    Computes Service Performance Score (0-100).
    Higher delays / higher response time -> lower score.
    """
    delay_norm = min_max_normalize(df["avg_delivery_delay_days"])
    resp_time_norm = min_max_normalize(df["avg_response_time_hours"])

    # Invert so higher performance gets higher score
    service_score = (
        0.50 * (100.0 - delay_norm) +
        0.50 * (100.0 - resp_time_norm)
    )
    return service_score.round(2)


def compute_opportunity_scoring(area_df):
    """
    Calculates final composite Opportunity Score:
    0.35 * Market Potential
  + 0.30 * Growth Rate Score
  + 0.20 * Penetration Gap (100 - current penetration)
  + 0.15 * Service Performance Score
    """
    df = area_df.copy()

    # 1. Market Potential Score & Growth Score
    mkt_pot_score, growth_norm = calculate_market_potential_score(df)
    df["market_potential_score"] = mkt_pot_score
    df["growth_score"] = growth_norm.round(2)

    # 2. Penetration Gap
    df["penetration_gap"] = (100.0 - df["current_penetration_rate"]).clip(0, 100).round(2)

    # 3. Service Performance Score
    df["service_performance_score"] = calculate_service_performance_score(df)

    # 4. Opportunity Score Composite Calculation
    opportunity_score = (
        0.35 * df["market_potential_score"] +
        0.30 * df["growth_score"] +
        0.20 * df["penetration_gap"] +
        0.15 * df["service_performance_score"]
    )
    df["opportunity_score"] = opportunity_score.round(2)

    # 5. Ranking and Classification
    df = df.sort_values(by="opportunity_score", ascending=False).reset_index(drop=True)
    df["opportunity_rank"] = df.index + 1

    def classify_opportunity(score):
        if score >= 75.0:
            return "High Opportunity"
        elif score >= 50.0:
            return "Medium Opportunity"
        else:
            return "Low Opportunity"

    df["opportunity_category"] = df["opportunity_score"].apply(classify_opportunity)

    return df


if __name__ == "__main__":
    from src.feature_engineering import run_feature_engineering_pipeline
    area_metrics = run_feature_engineering_pipeline()
    scored_df = compute_opportunity_scoring(area_metrics)
    print("\nOpportunity Scoring & Ranking Summary:")
    print(scored_df[[
        "opportunity_rank", "taluka", "opportunity_score", "opportunity_category",
        "market_potential_score", "current_penetration_rate", "penetration_gap",
        "service_performance_score"
    ]].to_string())
