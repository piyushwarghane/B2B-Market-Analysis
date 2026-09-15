"""
Root Cause Analysis Module.
Diagnoses why underperforming high-potential areas have low sales or penetration.
Evaluates 3 primary dimensions: Demand Gap, Distribution Gap, and Service Gap.
Generates automated root-cause diagnoses and actionable business recommendations.
"""

import pandas as pd
import numpy as np


def evaluate_root_causes(scored_df):
    """
    Performs multi-vector root cause analysis for each area.
    
    Inputs evaluated:
    - Demand Gap: Industrial density, estimated market size, YoY growth rate.
    - Distribution Gap: Active dealers, dealers per 100 industrial units.
    - Service Gap: Avg delivery delay days, avg response time hours, service delay %.
    """
    df = scored_df.copy()
    
    primary_gaps = []
    gap_details = []
    recommendations = []
    demand_gap_scores = []
    dist_gap_scores = []
    service_gap_scores = []

    for _, row in df.iterrows():
        # 1. Demand Gap Indicator (0-100 severity, 100 = severe demand constraint)
        # Low industrial density, low market size, low growth -> high demand gap
        demand_severity = 0.0
        if row["industrial_density"] < 60:
            demand_severity += 40.0
        if row["estimated_market_size"] < 45000000.0:
            demand_severity += 35.0
        if row["yoy_growth_rate"] < 7.5:
            demand_severity += 25.0
        demand_gap_scores.append(round(demand_severity, 2))

        # 2. Distribution Gap Indicator (0-100 severity, 100 = severe distribution bottleneck)
        # Low dealer count or dealers per 100 units < 0.25 -> high distribution gap
        dist_severity = 0.0
        dealers_per_100 = row["dealers_per_100_units"]
        if dealers_per_100 < 0.15:
            dist_severity += 50.0
        elif dealers_per_100 < 0.30:
            dist_severity += 30.0
            
        if row["dealer_count"] <= 1:
            dist_severity += 40.0
        elif row["dealer_count"] <= 2:
            dist_severity += 20.0
        dist_gap_scores.append(round(dist_severity, 2))

        # 3. Service Gap Indicator (0-100 severity, 100 = severe delivery & service failure)
        service_severity = 0.0
        if row["avg_delivery_delay_days"] > 2.5:
            service_severity += 45.0
        elif row["avg_delivery_delay_days"] > 1.0:
            service_severity += 25.0
            
        if row["avg_response_time_hours"] > 36.0:
            service_severity += 35.0
        elif row["avg_response_time_hours"] > 20.0:
            service_severity += 20.0
            
        if row["service_delay_pct"] > 20.0:
            service_severity += 20.0
        service_gap_scores.append(round(service_severity, 2))

        # Determine Primary Root Cause
        severities = {
            "Distribution Gap": dist_severity,
            "Service Gap": service_severity,
            "Demand Gap": demand_severity,
        }
        
        # Sort by severity
        sorted_severities = sorted(severities.items(), key=lambda x: x[1], reverse=True)
        top_gap, top_score = sorted_severities[0]

        # If top score is very low and penetration is high -> Mature Market / Optimized
        if top_score < 25.0 and row["current_penetration_rate"] > 50.0:
            primary_gap = "Market Optimized (Low Gap)"
            detail = "High market penetration supported by strong dealer network and reliable delivery service."
            rec = "Maintain current dealer incentives and optimize key enterprise customer retention."
        elif top_gap == "Distribution Gap":
            primary_gap = "Distribution Gap"
            detail = f"Severe channel under-coverage with only {row['dealer_count']} dealer(s) for {row['estimated_industrial_units']} industrial units."
            rec = "Expand authorized dealer network, onboard 2+ local tier-1 distributors, and establish a local stocking hub."
        elif top_gap == "Service Gap":
            primary_gap = "Service Gap"
            detail = f"High fulfillment bottleneck with {row['avg_delivery_delay_days']:.1f} days average delay and {row['avg_response_time_hours']:.0f}h response time."
            rec = "Establish a localized regional micro-warehouse, enforce SLA performance penalties, and optimize dispatch logistics."
        else:  # Demand Gap
            primary_gap = "Demand Gap"
            detail = f"Macro industrial scale constraint: market size {row['estimated_market_size']/1e6:.1f}M INR and low industrial density ({row['industrial_density']})."
            rec = "Adopt a targeted key-account sales strategy rather than broad distribution expansion."

        primary_gaps.append(primary_gap)
        gap_details.append(detail)
        recommendations.append(rec)

    df["demand_gap_score"] = demand_gap_scores
    df["distribution_gap_score"] = dist_gap_scores
    df["service_gap_score"] = service_gap_scores
    df["primary_root_cause"] = primary_gaps
    df["root_cause_details"] = gap_details
    df["recommended_action"] = recommendations

    return df


if __name__ == "__main__":
    from src.feature_engineering import run_feature_engineering_pipeline
    from src.opportunity_model import compute_opportunity_scoring

    area_metrics = run_feature_engineering_pipeline()
    scored_df = compute_opportunity_scoring(area_metrics)
    root_cause_df = evaluate_root_causes(scored_df)

    print("\nRoot Cause Analysis Summary:")
    print(root_cause_df[[
        "opportunity_rank", "taluka", "opportunity_score", "primary_root_cause", "recommended_action"
    ]].to_string())
