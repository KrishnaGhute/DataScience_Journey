# ==========================================================
# utils/charts.py
# Reservoir Monitoring System
# Plotly Chart Library
# ==========================================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# COMMON LAYOUT
# ==========================================================

def apply_layout(
    fig,
    title,
    showlegend=True,
    height=520
):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.01,
            xanchor="left",
            font=dict(
                size=22,
                family="Arial"
            )
        ),

        template="plotly_dark",

        height=height,

        hovermode="x unified",

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),
        
        showlegend=showlegend,

        legend=dict(

            orientation="h",

            yanchor="bottom",

            y=1.02,

            xanchor="right",

            x=1,

            bgcolor="rgba(0,0,0,0)",

            font=dict(size=13)

        )

    )

    fig.update_xaxes(

        title="Date",

        showgrid=False,

        rangeslider=dict(
            visible=True,
            thickness=0.05
        ),

        rangeselector=dict(

            buttons=[

                dict(
                    count=1,
                    label="1M",
                    step="month",
                    stepmode="backward"
                ),

                dict(
                    count=6,
                    label="6M",
                    step="month",
                    stepmode="backward"
                ),

                dict(
                    count=1,
                    label="1Y",
                    step="year",
                    stepmode="backward"
                ),

                dict(
                    step="all",
                    label="All"
                )

            ]

        )

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor="rgba(255,255,255,0.08)",

        zeroline=False

    )

    return fig


# ==========================================================
# STORAGE TREND
# ==========================================================

def storage_trend_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])
    df = df.sort_values("record_date")

    max_row = df.loc[df["current_storage"].idxmax()]
    min_row = df.loc[df["current_storage"].idxmin()]

    avg_storage = df["current_storage"].mean()

    fig = go.Figure()

    # --------------------------------------------------
    # Storage Line
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=df["record_date"],

            y=df["current_storage"],

            mode="lines",

            name="Storage",

            line=dict(
                color="#00BFFF",
                width=3
            ),

            fill="tozeroy",

            fillcolor="rgba(0,191,255,0.15)",

            hovertemplate=

            "<b>Date</b>: %{x}<br>" +

            "<b>Storage</b>: %{y:,.0f} MCFT<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Highest Storage
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=[max_row["record_date"]],

            y=[max_row["current_storage"]],

            mode="markers",

            name="Highest",

            marker=dict(

                color="#2ECC71",

                size=13,

                symbol="diamond"

            ),

            hovertemplate=

            "<b>Highest Storage</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Lowest Storage
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=[min_row["record_date"]],

            y=[min_row["current_storage"]],

            mode="markers",

            name="Lowest",

            marker=dict(

                color="#E74C3C",

                size=13,

                symbol="diamond"

            ),

            hovertemplate=

            "<b>Lowest Storage</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Average Storage Line
    # --------------------------------------------------

    fig.add_hline(

        y=avg_storage,

        line_dash="dash",

        line_color="orange"

    )

    # --------------------------------------------------
    # Common Layout
    # --------------------------------------------------

    apply_layout(

        fig,

        title="📈 Historical Reservoir Storage",

        showlegend=False

    )

    fig.update_yaxes(

        title="Storage (MCFT)"

    )

    return fig


# ==========================================================
# WATER LEVEL TREND
# ==========================================================

def water_level_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])
    df = df.sort_values("record_date")

    max_row = df.loc[df["current_level"].idxmax()]
    min_row = df.loc[df["current_level"].idxmin()]

    avg_level = df["current_level"].mean()

    fig = go.Figure()

    # --------------------------------------------------
    # Water Level Line
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=df["record_date"],

            y=df["current_level"],

            mode="lines",

            name="Water Level",

            line=dict(
                color="#3498DB",
                width=3
            ),

            fill="tozeroy",

            fillcolor="rgba(52,152,219,0.15)",

            hovertemplate=

            "<b>Date</b>: %{x}<br>" +

            "<b>Water Level</b>: %{y:.2f} ft<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Highest Level
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=[max_row["record_date"]],

            y=[max_row["current_level"]],

            mode="markers",

            marker=dict(
                color="#2ECC71",
                size=13,
                symbol="diamond"
            ),

            hovertemplate=

            "<b>Highest Level</b><br>%{y:.2f} ft<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Lowest Level
    # --------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=[min_row["record_date"]],

            y=[min_row["current_level"]],

            mode="markers",

            marker=dict(
                color="#E74C3C",
                size=13,
                symbol="diamond"
            ),

            hovertemplate=

            "<b>Lowest Level</b><br>%{y:.2f} ft<extra></extra>"

        )

    )

    # --------------------------------------------------
    # Average Water Level
    # --------------------------------------------------

    fig.add_hline(

        y=avg_level,

        line_dash="dash",

        line_color="orange"

    )

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------

    apply_layout(

        fig,

        title="📏 Historical Water Level",

        showlegend=False

    )

    fig.update_yaxes(

        title="Water Level (ft)"

    )

    return fig


# ==========================================================
# INFLOW VS OUTFLOW
# ==========================================================

def flow_comparison_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])
    df = df.sort_values("record_date")

    avg_inflow = df["current_inflow"].mean()
    avg_outflow = df["current_outflow"].mean()

    max_inflow = df.loc[df["current_inflow"].idxmax()]
    max_outflow = df.loc[df["current_outflow"].idxmax()]

    fig = go.Figure()

    # ======================================================
    # INFLOW
    # ======================================================

    fig.add_trace(

        go.Scatter(

            x=df["record_date"],

            y=df["current_inflow"],

            mode="lines",

            name="Inflow",

            line=dict(
                color="#2ECC71",
                width=3
            ),

            hovertemplate=

            "<b>Date</b>: %{x}<br>" +

            "<b>Inflow</b>: %{y:,.0f}<extra></extra>"

        )

    )

    # ======================================================
    # OUTFLOW
    # ======================================================

    fig.add_trace(

        go.Scatter(

            x=df["record_date"],

            y=df["current_outflow"],

            mode="lines",

            name="Outflow",

            line=dict(
                color="#E74C3C",
                width=3
            ),

            hovertemplate=

            "<b>Date</b>: %{x}<br>" +

            "<b>Outflow</b>: %{y:,.0f}<extra></extra>"

        )

    )

    # ======================================================
    # PEAK INFLOW
    # ======================================================

    fig.add_trace(

        go.Scatter(

            x=[max_inflow["record_date"]],

            y=[max_inflow["current_inflow"]],

            mode="markers",

            marker=dict(
                size=13,
                color="#2ECC71",
                symbol="diamond"
            ),

            showlegend=False,

            hovertemplate=

            "<b>Peak Inflow</b><br>%{y:,.0f}<extra></extra>"

        )

    )

    # ======================================================
    # PEAK OUTFLOW
    # ======================================================

    fig.add_trace(

        go.Scatter(

            x=[max_outflow["record_date"]],

            y=[max_outflow["current_outflow"]],

            mode="markers",

            marker=dict(
                size=13,
                color="#E74C3C",
                symbol="diamond"
            ),

            showlegend=False,

            hovertemplate=

            "<b>Peak Outflow</b><br>%{y:,.0f}<extra></extra>"

        )

    )

    # ======================================================
    # AVERAGE LINES
    # ======================================================

    fig.add_hline(

        y=avg_inflow,

        line_dash="dash",

        line_color="#2ECC71"

    )

    fig.add_hline(

        y=avg_outflow,

        line_dash="dash",

        line_color="#E74C3C"

    )

    # ======================================================
    # LAYOUT
    # ======================================================

    apply_layout(

        fig,

        title="🌊 Hydrological Flow Dynamics",

        showlegend=True

    )

    fig.update_yaxes(

        title="Flow Rate (MCFT/day)"

    )

    return fig


# ==========================================================
# MONTHLY STORAGE
# ==========================================================

def monthly_storage_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])

    monthly = (

        df

        .groupby(df["record_date"].dt.to_period("M"))

        ["current_storage"]

        .mean()

        .reset_index()

    )

    monthly["record_date"] = monthly["record_date"].dt.strftime("%b %Y")

    max_row = monthly.loc[monthly["current_storage"].idxmax()]
    min_row = monthly.loc[monthly["current_storage"].idxmin()]

    avg_storage = monthly["current_storage"].mean()

    colors = [

        "#00BFFF" if value >= avg_storage else "#1F4E79"

        for value in monthly["current_storage"]

    ]

    fig = go.Figure()

    # =====================================================
    # Monthly Bars
    # =====================================================

    fig.add_trace(

        go.Bar(

            x=monthly["record_date"],

            y=monthly["current_storage"],

            marker=dict(

                color=colors,

                line=dict(
                    color="white",
                    width=0.5
                )

            ),

            hovertemplate=

            "<b>%{x}</b><br>" +

            "Average Storage : %{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Average Line
    # =====================================================

    fig.add_hline(

        y=avg_storage,

        line_dash="dash",

        line_color="orange"

    )

    # =====================================================
    # Highest Month
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[max_row["record_date"]],

            y=[max_row["current_storage"]],

            mode="markers",

            marker=dict(

                size=14,

                color="#2ECC71",

                symbol="diamond"

            ),

            showlegend=False,

            hovertemplate=

            "<b>Highest Monthly Storage</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Lowest Month
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[min_row["record_date"]],

            y=[min_row["current_storage"]],

            mode="markers",

            marker=dict(

                size=14,

                color="#E74C3C",

                symbol="diamond"

            ),

            showlegend=False,

            hovertemplate=

            "<b>Lowest Monthly Storage</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Layout
    # =====================================================

    apply_layout(

        fig,

        title="📅 Monthly Average Storage",

        showlegend=False,

        height=500

    )

    fig.update_xaxes(

        title="Month",

        tickangle=-45,

        rangeslider_visible=False

    )

    fig.update_yaxes(

        title="Average Storage (MCFT)"

    )

    return fig

# ==========================================================
# YEARLY STORAGE
# ==========================================================

def yearly_storage_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])

    yearly = (

        df

        .groupby(df["record_date"].dt.year)

        ["current_storage"]

        .mean()

        .reset_index()

    )

    max_row = yearly.loc[yearly["current_storage"].idxmax()]
    min_row = yearly.loc[yearly["current_storage"].idxmin()]

    avg_storage = yearly["current_storage"].mean()

    fig = go.Figure()

    # =====================================================
    # Yearly Trend
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=yearly["record_date"],

            y=yearly["current_storage"],

            mode="lines+markers",

            line=dict(
                color="#00BFFF",
                width=3
            ),

            marker=dict(
                size=9,
                color="#00BFFF"
            ),

            fill="tozeroy",

            fillcolor="rgba(0,191,255,0.12)",

            hovertemplate=

            "<b>Year</b>: %{x}<br>" +

            "<b>Average Storage</b>: %{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Highest Year
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[max_row["record_date"]],

            y=[max_row["current_storage"]],

            mode="markers",

            marker=dict(
                color="#2ECC71",
                size=14,
                symbol="diamond"
            ),

            showlegend=False,

            hovertemplate=

            "<b>Highest Year</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Lowest Year
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[min_row["record_date"]],

            y=[min_row["current_storage"]],

            mode="markers",

            marker=dict(
                color="#E74C3C",
                size=14,
                symbol="diamond"
            ),

            showlegend=False,

            hovertemplate=

            "<b>Lowest Year</b><br>%{y:,.0f} MCFT<extra></extra>"

        )

    )

    # =====================================================
    # Average Line
    # =====================================================

    fig.add_hline(

        y=avg_storage,

        line_dash="dash",

        line_color="orange"

    )

    # =====================================================
    # Layout
    # =====================================================

    apply_layout(

        fig,

        title="📅 Yearly Average Storage",

        showlegend=False,

        height=500

    )

    fig.update_xaxes(

        title="Year",

        rangeslider_visible=False

    )

    fig.update_yaxes(

        title="Average Storage (MCFT)"

    )

    return fig


# ==========================================================
# STORAGE DISTRIBUTION
# ==========================================================

def storage_distribution_chart(df):

    df = pd.DataFrame(df).copy()

    fig = go.Figure()

    fig.add_trace(

        go.Histogram(

            x=df["current_storage"],

            nbinsx=30,

            marker=dict(
                color="#00BFFF",
                line=dict(
                    color="white",
                    width=1
                )
            ),

            hovertemplate=
            "<b>Storage Range</b><br>" +
            "%{x:,.0f} MCFT<br>" +
            "<b>Frequency</b>: %{y}<extra></extra>"

        )

    )

    apply_layout(

        fig,

        title="📊 Storage Distribution",

        showlegend=False,

        height=450

    )

    fig.update_xaxes(title="Storage (MCFT)")
    fig.update_yaxes(title="Frequency")

    return fig

# ==========================================================
# CAPACITY GAUGE
# ==========================================================

def capacity_gauge_chart(current_pct):

    fig = go.Figure()

    fig.add_trace(

        go.Indicator(

            mode="gauge+number",

            value=current_pct,

            number=dict(

                suffix="%",

                font=dict(
                    size=42,
                    color="white"
                )

            ),

            title=dict(

                text="<b>Reservoir Capacity Utilization</b>",

                font=dict(size=22)

            ),

            gauge=dict(

                axis=dict(

                    range=[0,100],

                    tickwidth=2,

                    tickcolor="white"

                ),

                bar=dict(

                    color="#00BFFF",

                    thickness=0.30

                ),

                steps=[

                    dict(range=[0,25],color="#8B0000"),

                    dict(range=[25,50],color="#E67E22"),

                    dict(range=[50,75],color="#F1C40F"),

                    dict(range=[75,100],color="#2ECC71")

                ],

                threshold=dict(

                    line=dict(

                        color="white",

                        width=4

                    ),

                    thickness=0.8,

                    value=current_pct

                )

            )

        )

    )

    fig.update_layout(

        template="plotly_dark",

        height=330,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    return fig

# ==========================================================
# CAPACITY COMPARISON
# ==========================================================

def capacity_bar_chart(df):

    df = pd.DataFrame(df).copy()

    df = df.sort_values("storage_pct", ascending=False)

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=df["dam_name"],

            y=df["storage_pct"],

            marker=dict(

                color=df["storage_pct"],

                colorscale="Viridis",

                showscale=False

            ),

            hovertemplate=

            "<b>%{x}</b><br>" +

            "Capacity : %{y:.1f}%<extra></extra>"

        )

    )

    apply_layout(

        fig,

        title="🏞 Reservoir Capacity Comparison",

        showlegend=False,

        height=500

    )

    fig.update_yaxes(title="Storage (%)")

    fig.update_xaxes(title="Reservoir")

    return fig

# ==========================================================
# STORAGE COMPARISON
# ==========================================================

def storage_bar_chart(df):

    df = pd.DataFrame(df).copy()

    df = df.sort_values("current_storage", ascending=False)

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=df["dam_name"],

            y=df["current_storage"],

            marker=dict(

                color=df["current_storage"],

                colorscale="Blues",

                showscale=False

            ),

            hovertemplate=

            "<b>%{x}</b><br>" +

            "Storage : %{y:,.0f} MCFT<extra></extra>"

        )

    )

    apply_layout(

        fig,

        title="💧 Current Water Storage Comparison",

        showlegend=False,

        height=500

    )

    fig.update_yaxes(title="Storage (MCFT)")

    fig.update_xaxes(title="Reservoir")

    return fig


# ==========================================================
# NET FLOW ANALYSIS
# ==========================================================

def net_flow_chart(df):

    df = pd.DataFrame(df).copy()

    df["record_date"] = pd.to_datetime(df["record_date"])
    df = df.sort_values("record_date")

    # --------------------------------------------------
    # Calculate Net Flow
    # --------------------------------------------------

    if "net_flow" not in df.columns:

        df["net_flow"] = (

            df["current_inflow"]

            -

            df["current_outflow"]

        )

    avg_flow = df["net_flow"].mean()

    max_gain = df.loc[df["net_flow"].idxmax()]
    max_loss = df.loc[df["net_flow"].idxmin()]

    colors = [

        "#2ECC71" if value >= 0 else "#E74C3C"

        for value in df["net_flow"]

    ]

    fig = go.Figure()

    # =====================================================
    # Net Flow Bars
    # =====================================================

    fig.add_trace(

        go.Bar(

            x=df["record_date"],

            y=df["net_flow"],

            marker_color=colors,

            hovertemplate=

            "<b>Date</b>: %{x}<br>" +

            "<b>Net Flow</b>: %{y:,.0f} MCFT/day<extra></extra>"

        )

    )

    # =====================================================
    # Maximum Gain
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[max_gain["record_date"]],

            y=[max_gain["net_flow"]],

            mode="markers",

            marker=dict(

                size=14,

                color="#2ECC71",

                symbol="diamond"

            ),

            showlegend=False,

            hovertemplate=

            "<b>Maximum Gain</b><br>%{y:,.0f} MCFT/day<extra></extra>"

        )

    )

    # =====================================================
    # Maximum Loss
    # =====================================================

    fig.add_trace(

        go.Scatter(

            x=[max_loss["record_date"]],

            y=[max_loss["net_flow"]],

            mode="markers",

            marker=dict(

                size=14,

                color="#E74C3C",

                symbol="diamond"

            ),

            showlegend=False,

            hovertemplate=

            "<b>Maximum Loss</b><br>%{y:,.0f} MCFT/day<extra></extra>"

        )

    )

    # =====================================================
    # Average Net Flow
    # =====================================================

    fig.add_hline(

        y=avg_flow,

        line_dash="dash",

        line_color="orange"

    )

    # =====================================================
    # Zero Reference
    # =====================================================

    fig.add_hline(

        y=0,

        line_color="white",

        line_width=2

    )

    # =====================================================
    # Layout
    # =====================================================

    apply_layout(

        fig,

        title="🔄 Reservoir Net Flow Analysis",

        showlegend=False

    )

    fig.update_yaxes(

        title="Net Flow (MCFT/day)"

    )

    return fig