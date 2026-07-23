# ==========================================================
# DAM ANALYSIS PAGE
# ==========================================================

import streamlit as st
import pandas as pd

from utils.database import (
    get_all_dams,
    get_dam_history
)

from utils.charts import (
    storage_trend_chart,
    flow_comparison_chart,
    capacity_gauge_chart,
    water_level_chart,
    net_flow_chart
)

from utils.plot_config import PLOT_CONFIG

from datetime import date
from datetime import timedelta

from utils.footer import app_footer
from utils.sidebar import app_sidebar

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Dam Analysis",
    page_icon="📈",
    layout="wide"
)

app_sidebar()

st.title("📈 Reservoir Analysis")
st.markdown("Analyze historical performance of an individual reservoir.")

st.divider()

# ==========================================================
# LOAD DAMS
# ==========================================================

with st.spinner("Loading reservoir data..."):
    
    dams = get_all_dams()

    if not dams:
        st.warning("No reservoirs found.")
        st.stop()

    dam_dict = {
        dam["dam_name"]: dam["dam_id"]
        for dam in dams
    }

# ==========================================================
# FILTER SECTION
# ==========================================================

MAX_DAYS = 1000

st.info(
    """
    ℹ️ **Analysis Range**

    For faster performance, the dashboard analyzes a maximum of **1000 daily records**
    (approximately **2.7 years**) at one time.
    """
)

# ---------------------------------------
# Reservoir Selection
# ---------------------------------------

selected_dam = st.selectbox(
    "🏞 Select Reservoir",
    list(dam_dict.keys())
)

# ---------------------------------------
# Date Selection
# ---------------------------------------

col1, col2 = st.columns(2)

with col1:

    start_date = st.date_input(
        "📅 Start Date",
        value=date(2018, 1, 1),
        min_value=date(2018, 1, 1),
        max_value=date(2025, 12, 31)
    )

# Automatically move end date 1000 days ahead
default_end = min(
    start_date + timedelta(days=MAX_DAYS),
    date(2025, 12, 31)
)

with col2:

    end_date = st.date_input(
        "📅 End Date",
        value=default_end,
        min_value=start_date,
        max_value=default_end
    )

# ---------------------------------------
# Information
# ---------------------------------------

st.caption(
    f"📅 Analysis Period : **{start_date.strftime('%d %b %Y')} → {end_date.strftime('%d %b %Y')}** "
    f"({(end_date-start_date).days} Days)"
)

# ==========================================================
# LOAD HISTORY
# ==========================================================

history = get_dam_history(
    dam_dict[selected_dam],
    start_date,
    end_date
)

if not history:
    st.warning("No records available for selected duration.")
    st.stop()

df = pd.DataFrame(history)

df["record_date"] = pd.to_datetime(df["record_date"])

df = df.sort_values("record_date")

# ==========================================================
# LATEST RECORD
# ==========================================================

latest = df.iloc[-1]

storage = latest["current_storage"]
level = latest["current_level"]
inflow = latest["current_inflow"]
outflow = latest["current_outflow"]
capacity = latest["storage_pct"]

# ==========================================================
# KPI CARDS
# ==========================================================

st.subheader("📊 Latest Reservoir Status")

latest_date = latest["record_date"].strftime("%d %b %Y")

st.info(
    f"These metrics are from the latest available record in the selected date range (**{latest_date}**)."
)

k1,k2,k3,k4,k5 = st.columns(5)

k1.metric(
    "💧 Storage",
    f"{storage:,.0f} MCFT"
)

k2.metric(
    "📏 Water Level",
    f"{level:.2f} ft"
)

k3.metric(
    "🌊 Inflow",
    f"{inflow:,.0f}"
)

k4.metric(
    "🚰 Outflow",
    f"{outflow:,.0f}"
)

k5.metric(
    "📊 Capacity",
    f"{capacity:.2f}%"
)

st.divider()

# ==========================================================
# RESERVOIR STATUS PANEL
# ==========================================================

st.subheader("🎯 Reservoir Status")

col1, col2 = st.columns([2, 1])

# ----------------------------------------------------------
# LEFT : Capacity Gauge
# ----------------------------------------------------------

with col1:

    st.plotly_chart(
        capacity_gauge_chart(capacity),
        use_container_width=True,
        config=PLOT_CONFIG
    )

# ----------------------------------------------------------
# RIGHT : Status Information
# ----------------------------------------------------------

with col2:

    st.markdown("### 📋 Current Status")

    st.metric(
        "Observation Date",
        latest["record_date"].strftime("%d %b %Y")
    )

    if capacity >= 90:
        st.success("🟦 Reservoir Nearly Full")

    elif capacity >= 70:
        st.success("🟢 Healthy Storage")

    elif capacity >= 50:
        st.warning("🟡 Moderate Storage")

    elif capacity >= 25:
        st.warning("🟠 Low Storage")

    else:
        st.error("🔴 Critical Storage")

    st.metric(
        "Storage Utilization",
        f"{capacity:.2f}%"
    )

st.divider()

# ==========================================================
# HISTORICAL ANALYTICS
# ==========================================================

st.subheader("📈 Historical Reservoir Analytics")

st.caption(
    "Interactive visual analytics of the selected reservoir during the selected date range."
)

# ==========================================================
# STORAGE TREND (MAIN CHART)
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📈 Highest Storage",
        f"{df['current_storage'].max():,.0f} MCFT"
    )

with col2:
    st.metric(
        "📉 Lowest Storage",
        f"{df['current_storage'].min():,.0f} MCFT"
    )

with col3:
    st.metric(
        "📊 Average Storage",
        f"{df['current_storage'].mean():,.0f} MCFT"
    )

st.plotly_chart(
    storage_trend_chart(df),
    use_container_width=True,
    config=PLOT_CONFIG
)

st.caption(
    "Shows historical variation of reservoir storage during the selected period."
)

st.divider()

# ==========================================================
# HYDROLOGICAL ANALYSIS
# ==========================================================

st.subheader("🌊 Hydrological Analysis")

st.divider()

left, right = st.columns(2)

# ----------------------------------------------------------

with left:
    
    st.markdown("### 🌊 Inflow vs Outflow")

    st.plotly_chart(
        flow_comparison_chart(df),
        use_container_width=True,
        config=PLOT_CONFIG
    )

    st.caption(
        "Comparison of daily inflow and outflow rates."
    )

# ----------------------------------------------------------

with right:
    
    st.markdown("### 📏 Water Level")

    st.plotly_chart(
        water_level_chart(df),
        use_container_width=True,
        config=PLOT_CONFIG
    )

    st.caption(
        "Variation in reservoir water level over time."
    )

st.divider()

# ==========================================================
# FLOW ANALYSIS
# ==========================================================

st.subheader("💧 Net Flow Analysis")

left2, right2 = st.columns([2,1])

# ----------------------------------------------------------

with left2:

    st.markdown("### 🔄 Net Flow")
    
    st.divider()

    st.plotly_chart(
        net_flow_chart(df),
        use_container_width=True,
        config=PLOT_CONFIG
    )

    st.caption(
        "Positive values indicate storage gain. Negative values indicate storage loss."
    )

# ----------------------------------------------------------

with right2:
    st.markdown("### 📊 Quick Statistics")

    st.metric(
        "Average Inflow",
        f"{df['current_inflow'].mean():,.0f}"
    )

    st.metric(
        "Average Outflow",
        f"{df['current_outflow'].mean():,.0f}"
    )

    st.metric(
        "Average Water Level",
        f"{df['current_level'].mean():.2f}"
    )

    st.metric(
        "Average Capacity",
        f"{df['storage_pct'].mean():.2f}%"
    )

st.divider()


# ==========================================================
# RESERVOIR INSIGHTS
# ==========================================================

st.subheader("🧠 Reservoir Insights")

latest = df.iloc[-1]
first = df.iloc[0]

storage_change = latest["current_storage"] - first["current_storage"]
capacity_change = latest["storage_pct"] - first["storage_pct"]

avg_inflow = df["current_inflow"].mean()
avg_outflow = df["current_outflow"].mean()

highest_storage = df["current_storage"].max()
lowest_storage = df["current_storage"].min()

highest_level = df["current_level"].max()
lowest_level = df["current_level"].min()

net = avg_inflow - avg_outflow

insight1, insight2 = st.columns(2)

# ----------------------------------------------------

with insight1:

    st.success("### 📈 Storage Analysis")

    if storage_change > 0:

        st.write(
            f"""
✅ Storage increased by **{storage_change:,.0f} MCFT**
during the selected period.
"""
        )

    else:

        st.write(
            f"""
⚠ Storage decreased by **{abs(storage_change):,.0f} MCFT**
during the selected period.
"""
        )

    st.write("")

    st.write(f"Highest Storage : **{highest_storage:,.0f} MCFT**")

    st.write(f"Lowest Storage : **{lowest_storage:,.0f} MCFT**")

# ----------------------------------------------------

with insight2:

    st.info("### 🌊 Hydrological Analysis")

    if net > 0:

        st.write(
            f"""
💧 Average inflow exceeded outflow by

**{net:,.0f}**

Reservoir gained water overall.
"""
        )

    else:

        st.write(
            f"""
🚰 Average outflow exceeded inflow by

**{abs(net):,.0f}**

Reservoir lost water overall.
"""
        )

    st.write("")

    st.write(f"Highest Water Level : **{highest_level:.2f} ft**")

    st.write(f"Lowest Water Level : **{lowest_level:.2f} ft**")

st.divider()


# ==========================================================
# STATISTICS
# ==========================================================

st.subheader("📊 Statistical Summary")

stats1, stats2, stats3, stats4 = st.columns(4)

stats1.metric(
    "Maximum Storage",
    f"{df['current_storage'].max():,.0f} MCFT"
)

stats2.metric(
    "Minimum Storage",
    f"{df['current_storage'].min():,.0f} MCFT"
)

stats3.metric(
    "Average Storage",
    f"{df['current_storage'].mean():,.0f} MCFT"
)

stats4.metric(
    "Records",
    f"{len(df):,}"
)

stats5, stats6, stats7, stats8 = st.columns(4)

stats5.metric(
    "Maximum Level",
    f"{df['current_level'].max():.2f} ft"
)

stats6.metric(
    "Average Inflow",
    f"{df['current_inflow'].mean():,.2f}"
)

stats7.metric(
    "Average Outflow",
    f"{df['current_outflow'].mean():,.2f}"
)

stats8.metric(
    "Average Capacity",
    f"{df['storage_pct'].mean():.2f}%"
)

st.divider()

# ==========================================================
# AI INSIGHTS
# ==========================================================

st.subheader("🧠 Reservoir Insights")

latest_storage = df.iloc[-1]["current_storage"]
first_storage = df.iloc[0]["current_storage"]

change = latest_storage - first_storage

if change > 0:
    trend = "📈 Increased"
elif change < 0:
    trend = "📉 Decreased"
else:
    trend = "➡ No Change"

st.info(f"""
### Analysis Summary

• Reservoir : **{selected_dam}**

• Analysis Period : **{start_date} → {end_date}**

• Storage Trend : **{trend}**

• Net Storage Change : **{change:,.2f} MCFT**

• Highest Storage Recorded : **{df['current_storage'].max():,.2f} MCFT**

• Lowest Storage Recorded : **{df['current_storage'].min():,.2f} MCFT**

• Average Capacity Utilization : **{df['storage_pct'].mean():.2f}%**

• Average Daily Inflow : **{df['current_inflow'].mean():,.2f}**

• Average Daily Outflow : **{df['current_outflow'].mean():,.2f}**
""")

st.divider()

# ==========================================================
# RESERVOIR INSPECTION REPORT
# ==========================================================

st.subheader("📑 Reservoir Inspection Report")

# ----------------------------------------------------------
# Current Snapshot
# ----------------------------------------------------------

latest = df.iloc[-1]

highest_storage = df.loc[df["current_storage"].idxmax()]
lowest_storage = df.loc[df["current_storage"].idxmin()]

highest_inflow = df.loc[df["current_inflow"].idxmax()]
highest_outflow = df.loc[df["current_outflow"].idxmax()]

max_gain = df.loc[df["net_flow"].idxmax()]
max_loss = df.loc[df["net_flow"].idxmin()]

# ----------------------------------------------------------
# Reservoir Information
# ----------------------------------------------------------

dam_name = df["dam_name"].iloc[0]
river = df["river"].iloc[0]
state = df["state"].iloc[0]
full_capacity = df["full_capacity"].iloc[0]

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

report = f"""
## 🏞 Reservoir Information

| Parameter | Value |
|------------|-------|
| **Reservoir Name** | {dam_name} |
| **River** | {river} |
| **State** | {state} |
| **Full Storage Capacity** | {full_capacity:,.0f} MCFT |

---

## 📅 Analysis Period

The selected analysis covers data from **{df['record_date'].min().strftime('%d %B %Y')}**
to **{df['record_date'].max().strftime('%d %B %Y')}**, consisting of
**{len(df)} daily observations**.

---

## 💧 Current Reservoir Condition

- **Current Storage:** {latest['current_storage']:,.0f} MCFT
- **Capacity Utilization:** {latest['storage_pct']:.2f} %
- **Current Water Level:** {latest['current_level']:.2f} ft
- **Current Daily Inflow:** {latest['current_inflow']:,.0f} MCFT/day
- **Current Daily Outflow:** {latest['current_outflow']:,.0f} MCFT/day

---

## 📊 Storage Analysis

- Highest Storage Recorded:
  **{highest_storage['current_storage']:,.0f} MCFT**
  on **{highest_storage['record_date'].strftime('%d %B %Y')}**

- Lowest Storage Recorded:
  **{lowest_storage['current_storage']:,.0f} MCFT**
  on **{lowest_storage['record_date'].strftime('%d %B %Y')}**

- Average Storage during the selected period:
  **{df['current_storage'].mean():,.0f} MCFT**

---

## 🌊 Hydrological Behaviour

- Maximum Daily Inflow:
  **{highest_inflow['current_inflow']:,.0f} MCFT/day**

- Maximum Daily Outflow:
  **{highest_outflow['current_outflow']:,.0f} MCFT/day**

- Largest Positive Net Flow:
  **{max_gain['net_flow']:,.0f} MCFT/day**

- Largest Negative Net Flow:
  **{max_loss['net_flow']:,.0f} MCFT/day**

---

## 📏 Water Level Analysis

- Highest Water Level:
  **{df['current_level'].max():.2f} ft**

- Lowest Water Level:
  **{df['current_level'].min():.2f} ft**

- Average Water Level:
  **{df['current_level'].mean():.2f} ft**

---

## 📌 Overall Assessment

The selected time period indicates the historical operating behaviour of the reservoir.

The visualizations presented above allow users to monitor changes in:

- Reservoir Storage
- Water Level
- Daily Inflow
- Daily Outflow
- Net Water Movement

These observations support informed reservoir operation, water resource planning, and historical performance analysis.

---

*Generated automatically by the Reservoir Monitoring System.*
"""

with st.container(border=True):
    st.markdown(report)

# ==========================================================
# HISTORICAL DATA
# ==========================================================

st.subheader("📋 Historical Records")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# DOWNLOAD
# ==========================================================

st.subheader("📥 Export Data")

csv = df.to_csv(index=False).encode("utf-8")

dam_name = df["dam_name"].iloc[0]

st.download_button(
    label="⬇ Download Selected Data (CSV)",
    data=csv,
    file_name=f"{dam_name}_analysis.csv",
    mime="text/csv"
)


app_footer()