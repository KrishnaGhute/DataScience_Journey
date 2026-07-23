# ==========================================================
# RESERVOIR COMPARISON DASHBOARD
# ==========================================================

import streamlit as st
import pandas as pd

from utils.database import (
    get_all_dams,
    get_dam_data
)

from utils.plot_config import PLOT_CONFIG

from utils.footer import app_footer

from utils.sidebar import app_sidebar
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Reservoir Comparison",
    page_icon="🔄",
    layout="wide"
)

app_sidebar()

st.title("🔄 Reservoir Comparison Dashboard")

st.caption(
    "Compare storage, water level, inflow, outflow, and operational performance across multiple reservoirs."
)

st.divider()

# ==========================================================
# LOAD RESERVOIRS
# ==========================================================
with st.spinner("Loading comparison dashboard..."):
    
    dams = get_all_dams()

    if len(dams) < 2:
        st.warning("At least two reservoirs are required for comparison.")
        st.stop()

    dam_dict = {
        d["dam_name"]: d
        for d in dams
    }

# ==========================================================
# RESERVOIR SELECTION
# ==========================================================

selected = st.multiselect(
    "🏞 Select Reservoirs (2–5)",
    options=list(dam_dict.keys()),
    default=list(dam_dict.keys())[:2],
    max_selections=5
)

if len(selected) < 2:
    st.info("Please select at least two reservoirs.")
    st.stop()

# ==========================================================
# LOAD LATEST RECORD OF EACH RESERVOIR
# ==========================================================

comparison = []

for dam in selected:

    dam_id = dam_dict[dam]["dam_id"]

    records = get_dam_data(dam_id)

    if len(records) == 0:
        continue

    latest = records[0].copy()

    latest["dam_name"] = dam

    comparison.append(latest)

if len(comparison) == 0:
    st.error("No data available.")
    st.stop()

comp_df = pd.DataFrame(comparison)

# ==========================================================
# CURRENT KPI COMPARISON
# ==========================================================

# ==========================================================
# CURRENT RESERVOIR STATUS
# ==========================================================

st.subheader("📊 Current Reservoir Status")

status_df = comp_df.copy()

status_df = status_df[[
    "dam_name",
    "current_storage",
    "storage_pct",
    "current_level",
    "current_inflow",
    "current_outflow"
]]

status_df.columns = [
    "Reservoir",
    "Storage (MCFT)",
    "Capacity (%)",
    "Water Level (ft)",
    "Inflow (MCFT/day)",
    "Outflow (MCFT/day)"
]

st.dataframe(
    status_df.style.format({
        "Storage (MCFT)": "{:,.0f}",
        "Capacity (%)": "{:.2f}",
        "Water Level (ft)": "{:.2f}",
        "Inflow (MCFT/day)": "{:,.0f}",
        "Outflow (MCFT/day)": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# STORAGE & CAPACITY COMPARISON
# ==========================================================

import plotly.express as px

st.subheader("💧 Storage Performance Comparison")

left, right = st.columns(2)

# ----------------------------------------------------------
# STORAGE
# ----------------------------------------------------------

with left:

    fig_storage = px.bar(

        comp_df.sort_values(
            "current_storage",
            ascending=False
        ),

        x="dam_name",

        y="current_storage",

        color="current_storage",

        color_continuous_scale="Blues",

        text="current_storage",

        title="Current Storage"
    )

    fig_storage.update_traces(

        texttemplate="%{text:,.0f}",

        textposition="outside"

    )

    fig_storage.update_layout(

        template="plotly_dark",

        font=dict(color="white"),

        showlegend=False,

        margin=dict(l=20,r=20,t=60,b=20),

        yaxis_title="Storage (MCFT)",

        xaxis_title=""
    )

    fig_storage.update_xaxes(showgrid=False)

    fig_storage.update_yaxes(
        gridcolor="rgba(255,255,255,0.08)"
    )

    st.plotly_chart(
        fig_storage,
        use_container_width=True,
        config=PLOT_CONFIG
    )

# ----------------------------------------------------------
# CAPACITY
# ----------------------------------------------------------

with right:

    fig_capacity = px.bar(

        comp_df.sort_values(
            "storage_pct",
            ascending=False
        ),

        x="dam_name",

        y="storage_pct",

        color="storage_pct",

        color_continuous_scale="Viridis",

        text="storage_pct",

        title="Capacity Utilization"
    )

    fig_capacity.update_traces(

        texttemplate="%{text:.1f}%",

        textposition="outside"

    )

    fig_capacity.update_layout(

        template="plotly_dark",

        font=dict(color="white"),

        showlegend=False,

        margin=dict(l=20,r=20,t=60,b=20),

        yaxis_title="Capacity (%)",

        xaxis_title=""
    )

    fig_capacity.update_xaxes(showgrid=False)

    fig_capacity.update_yaxes(
        gridcolor="rgba(255,255,255,0.08)"
    )

    st.plotly_chart(
        fig_capacity,
        use_container_width=True,
        config=PLOT_CONFIG
    )

st.divider()

# ==========================================================
# WATER LEVEL & FLOW COMPARISON
# ==========================================================

st.subheader("🌊 Hydrological Comparison")

left, right = st.columns(2)

# ----------------------------------------------------------
# WATER LEVEL
# ----------------------------------------------------------

with left:

    fig_level = px.bar(

        comp_df.sort_values(
            "current_level",
            ascending=False
        ),

        x="dam_name",

        y="current_level",

        color="current_level",

        color_continuous_scale="Teal",

        text="current_level",

        title="Water Level"
    )

    fig_level.update_traces(

        texttemplate="%{text:.2f}",

        textposition="outside"

    )

    fig_level.update_layout(

        template="plotly_dark",

        font=dict(color="white"),

        showlegend=False,

        margin=dict(l=20,r=20,t=60,b=20),

        yaxis_title="Level (ft)",

        xaxis_title=""
    )

    fig_level.update_xaxes(showgrid=False)

    fig_level.update_yaxes(
        gridcolor="rgba(255,255,255,0.08)"
    )

    st.plotly_chart(
        fig_level,
        use_container_width=True,
        config=PLOT_CONFIG
    )

# ----------------------------------------------------------
# INFLOW VS OUTFLOW
# ----------------------------------------------------------

with right:

    flow_df = comp_df.melt(

        id_vars="dam_name",

        value_vars=[
            "current_inflow",
            "current_outflow"
        ],

        var_name="Flow",

        value_name="MCFT"
    )

    flow_df["Flow"] = flow_df["Flow"].replace({

        "current_inflow":"Inflow",

        "current_outflow":"Outflow"

    })

    fig_flow = px.bar(

        flow_df,

        x="dam_name",

        y="MCFT",

        color="Flow",

        barmode="group",

        text="MCFT",

        title="Daily Inflow vs Outflow"
    )

    fig_flow.update_traces(

        texttemplate="%{text:,.0f}",

        textposition="outside"

    )

    fig_flow.update_layout(

        template="plotly_dark",

        font=dict(color="white"),

        margin=dict(l=20,r=20,t=60,b=20),

        yaxis_title="MCFT/day",

        xaxis_title=""
    )

    fig_flow.update_xaxes(showgrid=False)

    fig_flow.update_yaxes(
        gridcolor="rgba(255,255,255,0.08)"
    )

    st.plotly_chart(
        fig_flow,
        use_container_width=True,
        config=PLOT_CONFIG
    )

st.divider()

# ==========================================================
# RESERVOIR PERFORMANCE RANKINGS
# ==========================================================

st.subheader("🏆 Reservoir Performance Rankings")

left, right = st.columns(2)

# ----------------------------------------------------------
# LEFT
# ----------------------------------------------------------

with left:

    st.markdown("### 💧 Storage Rankings")

    storage_rank = (
        comp_df[
            ["dam_name", "current_storage"]
        ]
        .sort_values(
            "current_storage",
            ascending=False
        )
        .reset_index(drop=True)
    )

    for i, row in storage_rank.iterrows():

        medal = ["🥇", "🥈", "🥉"]

        icon = medal[i] if i < 3 else "•"

        st.write(
            f"{icon} **{row['dam_name']}** — {row['current_storage']:,.0f} MCFT"
        )

    st.divider()

    st.markdown("### 🌊 Highest Daily Inflow")

    inflow_rank = (
        comp_df[
            ["dam_name", "current_inflow"]
        ]
        .sort_values(
            "current_inflow",
            ascending=False
        )
        .reset_index(drop=True)
    )

    for i, row in inflow_rank.iterrows():

        medal = ["🥇", "🥈", "🥉"]

        icon = medal[i] if i < 3 else "•"

        st.write(
            f"{icon} **{row['dam_name']}** — {row['current_inflow']:,.0f} MCFT/day"
        )

# ----------------------------------------------------------
# RIGHT
# ----------------------------------------------------------

with right:

    st.markdown("### 📊 Capacity Rankings")

    cap_rank = (
        comp_df[
            ["dam_name", "storage_pct"]
        ]
        .sort_values(
            "storage_pct",
            ascending=False
        )
        .reset_index(drop=True)
    )

    for i, row in cap_rank.iterrows():

        medal = ["🥇", "🥈", "🥉"]

        icon = medal[i] if i < 3 else "•"

        st.write(
            f"{icon} **{row['dam_name']}** — {row['storage_pct']:.2f}%"
        )

    st.divider()

    st.markdown("### 📏 Water Level Rankings")

    level_rank = (
        comp_df[
            ["dam_name", "current_level"]
        ]
        .sort_values(
            "current_level",
            ascending=False
        )
        .reset_index(drop=True)
    )

    for i, row in level_rank.iterrows():

        medal = ["🥇", "🥈", "🥉"]

        icon = medal[i] if i < 3 else "•"

        st.write(
            f"{icon} **{row['dam_name']}** — {row['current_level']:.2f} ft"
        )

st.divider()

# ==========================================================
# QUICK OBSERVATIONS
# ==========================================================

st.subheader("📌 Key Observations")

highest_storage = comp_df.loc[
    comp_df["current_storage"].idxmax()
]

lowest_storage = comp_df.loc[
    comp_df["current_storage"].idxmin()
]

highest_capacity = comp_df.loc[
    comp_df["storage_pct"].idxmax()
]

highest_level = comp_df.loc[
    comp_df["current_level"].idxmax()
]

highest_inflow = comp_df.loc[
    comp_df["current_inflow"].idxmax()
]

highest_outflow = comp_df.loc[
    comp_df["current_outflow"].idxmax()
]

with st.container(border=True):

    st.markdown(f"""

### Executive Summary

• **{highest_storage['dam_name']}**
currently stores the largest volume of water
(**{highest_storage['current_storage']:,.0f} MCFT**).

• **{lowest_storage['dam_name']}**
has the lowest available storage
(**{lowest_storage['current_storage']:,.0f} MCFT**).

• **{highest_capacity['dam_name']}**
has the highest reservoir utilization
(**{highest_capacity['storage_pct']:.2f}%**).

• **{highest_level['dam_name']}**
currently has the highest water level
(**{highest_level['current_level']:.2f} ft**).

• **{highest_inflow['dam_name']}**
is receiving the largest daily inflow
(**{highest_inflow['current_inflow']:,.0f} MCFT/day**).

• **{highest_outflow['dam_name']}**
is releasing the highest daily outflow
(**{highest_outflow['current_outflow']:,.0f} MCFT/day**).

These observations summarize the operational status of the selected reservoirs and help identify leading reservoirs in terms of storage, utilization, inflow, and water level.

""")

st.divider()

# ==========================================================
# EXPORT
# ==========================================================

st.subheader("📥 Export Comparison Report")

csv = status_df.to_csv(index=False).encode("utf-8")

left, right = st.columns(2)

with left:

    st.download_button(

        label="⬇ Download Comparison (CSV)",

        data=csv,

        file_name="reservoir_comparison.csv",

        mime="text/csv"

    )

with right:

    report = f"""
Reservoir Comparison Report

Generated by:
Reservoir Monitoring System

====================================================

Reservoirs Compared

{", ".join(selected)}

====================================================

Highest Storage

{highest_storage['dam_name']}
{highest_storage['current_storage']:,.0f} MCFT

Lowest Storage

{lowest_storage['dam_name']}
{lowest_storage['current_storage']:,.0f} MCFT

Highest Capacity

{highest_capacity['dam_name']}
{highest_capacity['storage_pct']:.2f}%

Highest Water Level

{highest_level['dam_name']}
{highest_level['current_level']:.2f} ft

Highest Inflow

{highest_inflow['dam_name']}
{highest_inflow['current_inflow']:,.0f} MCFT/day

Highest Outflow

{highest_outflow['dam_name']}
{highest_outflow['current_outflow']:,.0f} MCFT/day

====================================================

Reservoir Details

"""

    for _, row in status_df.iterrows():

        report += f"""

----------------------------------------------------

Reservoir

{row['Reservoir']}

Storage

{row['Storage (MCFT)']:,.0f} MCFT

Capacity

{row['Capacity (%)']:.2f} %

Water Level

{row['Water Level (ft)']:.2f} ft

Inflow

{row['Inflow (MCFT/day)']:,.0f} MCFT/day

Outflow

{row['Outflow (MCFT/day)']:,.0f} MCFT/day

"""

    st.download_button(

        label="📄 Download Comparison Report",

        data=report,

        file_name="reservoir_comparison_report.txt",

        mime="text/plain"

    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.success(
    "✅ Comparison completed successfully. Use the charts, rankings, and detailed table above to evaluate reservoir performance across the selected reservoirs."
)

app_footer()