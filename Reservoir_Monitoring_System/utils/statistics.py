# ==========================================================
# utils/statistics.py
# Reservoir Monitoring System
# Statistical Analysis Utilities
# ==========================================================

import pandas as pd


def calculate_statistics(df):
    """
    Calculates important statistics for a reservoir.
    """

    if df is None or len(df) == 0:
        return {}

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])

    stats = {

        "total_records": len(df),

        "start_date": df["record_date"].min().date(),

        "end_date": df["record_date"].max().date(),

        "max_storage": round(df["current_storage"].max(),2),

        "min_storage": round(df["current_storage"].min(),2),

        "avg_storage": round(df["current_storage"].mean(),2),

        "max_level": round(df["current_level"].max(),2),

        "min_level": round(df["current_level"].min(),2),

        "avg_level": round(df["current_level"].mean(),2),

        "avg_inflow": round(df["current_inflow"].mean(),2),

        "avg_outflow": round(df["current_outflow"].mean(),2),

        "max_inflow": round(df["current_inflow"].max(),2),

        "max_outflow": round(df["current_outflow"].max(),2),

        "avg_capacity": round(df["storage_pct"].mean(),2),

        "max_capacity": round(df["storage_pct"].max(),2),

        "min_capacity": round(df["storage_pct"].min(),2),

        "net_flow": round(df["net_flow"].sum(),2)

    }

    return stats