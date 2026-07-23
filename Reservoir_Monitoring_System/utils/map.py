# ==========================================================
# utils/map.py
# Interactive Reservoir Map
# ==========================================================

import pandas as pd
import plotly.express as px
import streamlit as st


def render_dam_map(dams):

    if not dams:
        st.warning("No reservoir data available.")
        return

    df = pd.DataFrame(dams)

    required = [
        "latitude",
        "longitude",
        "dam_name",
        "storage_pct"
    ]

    for col in required:
        if col not in df.columns:
            st.error(f"Missing column: {col}")
            return

    # ---------------------------------------------------
    # Status
    # ---------------------------------------------------

    def get_status(x):
        if x < 30:
            return "Critical"
        elif x < 70:
            return "Moderate"
        return "Healthy"

    if "status" not in df.columns:
        df["status"] = df["storage_pct"].apply(get_status)

    # ---------------------------------------------------
    # Marker Size
    # ---------------------------------------------------

    if "current_storage" in df.columns:

        max_storage = df["current_storage"].max()

        df["marker_size"] = (
            (df["current_storage"] / max_storage) * 25
        ) + 10

    else:

        df["marker_size"] = 18

    # ---------------------------------------------------
    # Hover Information
    # ---------------------------------------------------

    hover = {
        "river": True,
        "current_storage": ":,.0f",
        "storage_pct": ":.2f",
        "current_level": ":.2f",
        "current_inflow": ":,.0f",
        "current_outflow": ":,.0f",
        "status": True
    }

    fig = px.scatter_map(
        df,

        lat="latitude",

        lon="longitude",

        color="status",

        size="marker_size",

        hover_name="dam_name",

        hover_data=hover,

        zoom=5,

        height=600,

        color_discrete_map={

            "Healthy": "#2ECC71",

            "Moderate": "#F1C40F",

            "Critical": "#E74C3C"

        }
    )

    fig.update_traces(

        marker=dict(
            opacity=0.90
        )
    )

    fig.update_layout(

        title="South India Reservoir Locations",

        map_style="open-street-map",

        margin=dict(
            l=0,
            r=0,
            t=50,
            b=0
        ),

        legend=dict(

            title="Reservoir Status",

            orientation="h",

            y=1.02,

            x=0

        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "🟢 Healthy (≥70%)   |   🟡 Moderate (30–70%)   |   🔴 Critical (<30%)"
    )