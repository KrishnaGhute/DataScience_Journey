import streamlit as st

from utils.footer import app_footer

from utils.sidebar import app_sidebar

st.set_page_config(
    page_title="Help",
    page_icon="❓",
    layout="wide"
)

app_sidebar()

st.title("❓ Help & User Guide")

st.caption(
    "Learn how to navigate and use the Reservoir Monitoring System."
)

st.divider()

# ==========================================================
# INTRODUCTION
# ==========================================================

st.header("👋 Welcome")

st.write("""
The Reservoir Monitoring System is designed to provide interactive
visualization and analysis of historical reservoir data.

This guide explains the purpose of each page and how to use the application.
""")

st.header("🚀 Quick Start Guide")

st.info("""
Follow these simple steps to explore the Reservoir Monitoring System.
""")

step1, step2, step3 = st.columns(3)

with step1:

    st.success("""
### ① Dashboard

View the overall condition of all monitored reservoirs, including
storage, inflow, outflow, and capacity utilization.
""")

with step2:

    st.success("""
### ② Dam Analysis

Select a reservoir to explore historical storage, water level,
net flow, and detailed analytical reports.
""")

with step3:

    st.success("""
### ③ Comparison

Select multiple reservoirs to compare storage,
capacity, water levels, inflow, and performance.
""")

st.divider()

step4, step5, step6 = st.columns(3)

with step4:

    st.success("""
### ④ Export Reports

Download reservoir datasets as CSV files
or generate professional PDF inspection reports.
""")

with step5:

    st.success("""
### ⑤ Administrator

Authorized users can add daily records,
upload datasets, and manage reservoir information.
""")

with step6:

    st.success("""
### ⑥ Future Forecasting

Machine learning–based reservoir storage forecasting
will be available in a future release.
""")

st.divider()

# ==========================================================
# DASHBOARD
# ==========================================================

with st.expander("📊 Dashboard", expanded=True):

    st.markdown("""
### Purpose

The Dashboard provides a real-time overview of all monitored reservoirs.

### Available Information

- Total water storage
- Total inflow and outflow
- Average reservoir capacity
- Interactive reservoir location map
- Storage comparison charts
- Capacity utilization charts

### Recommended Use

Use this page to quickly understand the overall status of all reservoirs.
""")

# ==========================================================
# DAM ANALYSIS
# ==========================================================

with st.expander("🏞 Dam Analysis"):

    st.markdown("""
### Purpose

Analyze one reservoir in detail.

### Available Features

- Historical storage trend
- Water level analysis
- Inflow and outflow analysis
- Net water movement
- Monthly and yearly summaries
- Capacity utilization
- PDF report generation
- CSV export

### Recommended Use

Use this page when detailed historical analysis of an individual reservoir is required.
""")

# ==========================================================
# COMPARISON
# ==========================================================

with st.expander("🔄 Reservoir Comparison"):

    st.markdown("""
### Purpose

Compare multiple reservoirs simultaneously.

### Available Features

- Storage comparison
- Capacity comparison
- Water level comparison
- Inflow comparison
- Outflow comparison
- Performance ranking
- Statistical comparison table

### Recommended Use

Useful for identifying differences between reservoirs and evaluating overall performance.
""")

# ==========================================================
# ABOUT
# ==========================================================

with st.expander("ℹ️ About"):

    st.markdown("""
Provides information about the project including:

- Project overview
- Technology stack
- Dataset summary
- Developer information
- Future development roadmap
""")

# ==========================================================
# ADMIN
# ==========================================================

with st.expander("🔐 Administrator"):

    st.markdown("""
Administrator functions are available only after successful authentication.

Authorized users can:

- Add daily reservoir records
- Upload historical datasets
- Manage reservoir information
- Maintain the central database
""")

# ==========================================================
# DATA
# ==========================================================

with st.expander("🗂 Dataset Information"):

    st.markdown("""
Current dataset includes:

- 19 South Indian reservoirs
- 55,500 historical daily observations
- Observation period: 2018–2025

Recorded parameters include:

- Water Storage
- Water Level
- Inflow
- Outflow
- Capacity Utilization
- Net Water Movement
""")

# ==========================================================
# EXPORT
# ==========================================================

with st.expander("📄 Export Options"):

    st.markdown("""
The application supports exporting analysis results.

Available formats:

- CSV
- PDF (Reservoir Inspection Report)

Exports contain only the currently selected or filtered data.
""")

# ==========================================================
# SUPPORT
# ==========================================================

st.divider()

st.header("📬 Support")

st.info("""
If you experience unexpected behaviour while using the application:

• Verify that the selected reservoir contains historical data.

• Ensure an internet connection is available for database access.

• Contact the developer for technical support or future enhancements.
""")


app_footer()