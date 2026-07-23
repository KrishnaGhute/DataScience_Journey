import pandas as pd


def latest_metrics(df):

    df = pd.DataFrame(df)

    if df.empty:
        return None

    df["record_date"] = pd.to_datetime(df["record_date"])

    latest = df.sort_values("record_date").iloc[-1]

    return {
        "storage": latest["current_storage"],
        "inflow": latest["current_inflow"],
        "outflow": latest["current_outflow"],
        "capacity": latest["storage_pct"],
    }