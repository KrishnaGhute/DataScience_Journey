# ==========================================================
# pages/1_Dashboard.py
# Reservoir Monitoring System v2
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import (
    get_latest_records,
    get_dashboard_summary
)

from utils.map import render_dam_map
from utils.plot_config import PLOT_CONFIG

from utils.footer import app_footer

from utils.sidebar import app_sidebar

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

app_sidebar()

st.title("🌊 South India Reservoir Monitoring System")

st.caption(
    "Real-time monitoring and operational overview of major reservoirs across South India."
)

# ==========================================================
# LOAD DATA
# ==========================================================

with st.spinner("Loading dashboard..."):

    summary = get_dashboard_summary()
    latest_records = get_latest_records()

    if not latest_records:
        st.warning("No reservoir data found.")
        st.stop()

    df = pd.DataFrame(latest_records)

# ==========================================================
# STATUS COLUMN
# ==========================================================

def storage_status(x):
    if x < 30:
        return "🔴 Critical"
    elif x < 70:
        return "🟡 Moderate"
    else:
        return "🟢 Healthy"

df["status"] = df["storage_pct"].apply(storage_status)

# ==========================================================
# KPI SECTION
# ==========================================================

st.subheader("📈 System Overview")

k1, k2, k3 = st.columns(3)

k1.metric(
    "💧 Total Storage",
    f"{summary['total_storage']:,.0f} MCFT",
    help="Combined water storage across all monitored reservoirs."
)

k2.metric(
    "🌊 Total Daily Inflow",
    f"{summary['total_inflow']:,.0f} MCFT",
    help="Total daily inflow into all monitored reservoirs."
)

k3.metric(
    "🚰 Total Daily Outflow",
    f"{summary['total_outflow']:,.0f} MCFT",
    help="Total daily outflow released from all monitored reservoirs."
)

k4, k5, k6 = st.columns(3)

k4.metric(
    "📊 Average Capacity",
    f"{summary['avg_capacity']:.2f}%",
    help="Average reservoir storage utilization."
)

k5.metric(
    "🏞 Monitored Reservoirs",
    f"{int(summary['total_dams'])}",
    help="Total number of reservoirs monitored."
)

k6.metric(
    "📅 Latest Observation",
    pd.to_datetime(summary["latest_update"]).strftime("%d %b %Y"),
    help="Most recent date for which reservoir data is available."
)

st.divider()

# ==========================================================
# MAP
# ==========================================================

st.subheader("🗺 Reservoir Locations")

# Prepare map dataframe
map_columns = [
    "dam_name",
    "latitude",
    "longitude",
    "storage_pct",
    "current_storage",
    "current_level",
    "current_inflow",
    "current_outflow",
    "river"
]

# Keep only available columns
available_columns = [
    col for col in map_columns 
    if col in df.columns
]

map_df = df[available_columns].copy()


# Remove invalid coordinates
map_df = map_df.dropna(
    subset=[
        "latitude",
        "longitude"
    ]
)


# Render interactive map
render_dam_map(
    map_df.to_dict("records")
)


st.divider()


# ==========================================================
# CHARTS
# ==========================================================

left, right = st.columns(2)

with left:

    fig_storage = px.bar(
        df.sort_values("current_storage", ascending=False),
        x="dam_name",
        y="current_storage",
        color="current_storage",
        title="Current Storage"
    )

    fig_storage.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_storage,
        use_container_width=True,
        config=PLOT_CONFIG
    )

with right:

    fig_capacity = px.bar(
        df.sort_values("storage_pct", ascending=False),
        x="dam_name",
        y="storage_pct",
        color="storage_pct",
        title="Capacity Utilization (%)"
    )

    fig_capacity.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_capacity,
        use_container_width=True,
        config=PLOT_CONFIG
    )

st.divider()

# ==========================================================
# STORAGE DISTRIBUTION
# ==========================================================

left, right = st.columns([2,1])

with left:

    fig_hist = px.histogram(
        df,
        x="current_storage",
        nbins=15,
        title="Storage Distribution"
    )

    fig_hist.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_hist,
        use_container_width=True,
        config=PLOT_CONFIG
    )

with right:

    fig_pie = px.pie(
        df,
        names="dam_name",
        values="current_storage",
        title="Storage Share"
    )

    fig_pie.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_pie,
        use_container_width=True,
        config=PLOT_CONFIG
    )

st.divider()

# ==========================================================
# TOP / BOTTOM
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top 5 Reservoirs")

    top5 = (
        df[
            ["dam_name", "current_storage", "storage_pct"]
        ]
        .sort_values("current_storage", ascending=False)
        .head(5)
    )

    st.dataframe(
        top5,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("⚠️ Lowest 5 Reservoirs")

    low5 = (
        df[
            ["dam_name", "current_storage", "storage_pct"]
        ]
        .sort_values("current_storage")
        .head(5)
    )

    st.dataframe(
        low5,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================================
# SEARCHABLE TABLE
# ==========================================================

st.subheader("📋 Latest Reservoir Status")

search = st.text_input(
    "🔍 Search Reservoir",
    placeholder="Type reservoir name..."
)

table = df.copy()

if search:
    table = table[
        table["dam_name"].str.contains(search, case=False)
    ]

display_cols = [
    "dam_name",
    "record_date",
    "current_storage",
    "current_level",
    "current_inflow",
    "current_outflow",
    "storage_pct",
    "status"
]

st.dataframe(
    table[display_cols],
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = table.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Latest Reservoir Data",
    csv,
    "latest_reservoir_status.csv",
    "text/csv",
    use_container_width=True
)

st.divider()

# ==========================================================
# INSIGHTS
# ==========================================================

highest = df.loc[df["storage_pct"].idxmax(), "dam_name"]
lowest = df.loc[df["storage_pct"].idxmin(), "dam_name"]

st.success(f"🏆 **{highest}** has the highest capacity utilization.")
st.warning(f"⚠️ **{lowest}** has the lowest capacity utilization.")

critical = len(df[df["storage_pct"] < 30])
healthy = len(df[df["storage_pct"] > 70])

st.info(f"💧 {healthy} reservoirs are above 70% capacity.")

if critical:
    st.error(f"🚨 {critical} reservoirs are below 30% capacity.")


app_footer()