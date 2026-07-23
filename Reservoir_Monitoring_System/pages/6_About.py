import streamlit as st

from utils.footer import app_footer

from utils.sidebar import app_sidebar

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

app_sidebar()

st.title("ℹ️ About Reservoir Monitoring System")

st.caption(
    "A Geospatial Reservoir Monitoring and Data Analytics Platform"
)

st.divider()

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📖 Project Overview")

st.write("""
The **Reservoir Monitoring System** is a web-based analytics platform designed
to monitor, visualize, and analyze historical reservoir conditions through an
interactive dashboard.

The application integrates spatial visualization, historical storage analysis,
comparative reservoir analytics, administrative data management, and reporting
into a single platform for reservoir monitoring and operational decision support.

The current version focuses on data visualization and analytics using historical
reservoir observations collected between **2018 and 2025**.
""")

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.header("🚀 Core Features")

left, right = st.columns(2)

with left:

    st.success("📊 Interactive Monitoring Dashboard")

    st.success("🗺 Interactive Reservoir Map")

    st.success("🏞 Individual Reservoir Analysis")

    st.success("🔄 Multi-Reservoir Comparison")

with right:

    st.success("📈 Historical Trend Analysis")

    st.success("📄 PDF & CSV Report Export")

    st.success("🔐 Secure Administrator Panel")

    st.success("🗂 Centralized Reservoir Database")

st.divider()

# ==========================================================
# TECHNOLOGY
# ==========================================================

st.header("💻 Technology Stack")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric("Programming", "Python")

    st.metric("Framework", "Streamlit")

with c2:

    st.metric("Database", "Supabase")

    st.metric("Visualization", "Plotly")

with c3:

    st.metric("Maps", "OpenStreetMap")

    st.metric("Data Processing", "Pandas")

st.divider()

# ==========================================================
# DATASET
# ==========================================================

st.header("🗂 Dataset")

a, b, c = st.columns(3)

a.metric("Reservoirs", "19")

b.metric("Historical Records", "55,500")

c.metric("Study Period", "2018–2025")

st.info("""
**Coverage:** South Indian Reservoirs

**Observation Frequency:** Daily

**Available Variables**

• Water Storage

• Water Level

• Reservoir Capacity

• Inflow

• Outflow

• Net Water Movement
""")

st.divider()

# ==========================================================
# PROJECT STATUS
# ==========================================================

st.header("📌 Current Development Status")

st.write("""
The Reservoir Monitoring System currently provides:

- Interactive geospatial visualization
- Reservoir performance monitoring
- Historical data analytics
- Comparative reservoir analysis
- Administrative data management
- Professional reporting and data export

Machine learning forecasting is planned for a future version of the platform.
""")

st.divider()

# ==========================================================
# DEVELOPER
# ==========================================================

st.header("👨‍💻 Developer")

left, right = st.columns([1,2])

with left:

    st.image(
        "assets/profile.jpg.png",
        use_container_width=True
    )

with right:

    st.markdown("""
## Krishna Ghute

**Data Science Professional**

Passionate about building intelligent data-driven systems using
analytics, geospatial visualization, and artificial intelligence.

### Areas of Interest

- Data Science
- Data Analytics
- Artificial Intelligence
- Machine Learning
- Geospatial Analytics
- Water Resource Intelligence
- Data Visualization
""")

st.divider()

# ==========================================================
# FUTURE ROADMAP
# ==========================================================

st.header("🛣 Product Roadmap")

st.checkbox("Machine Learning Forecasting", value=False, disabled=True)

st.checkbox("Weather Data Integration", value=False, disabled=True)

st.checkbox("Flood Risk Monitoring", value=False, disabled=True)

st.checkbox("Drought Intelligence", value=False, disabled=True)

st.checkbox("Real-Time Sensor Integration", value=False, disabled=True)

st.checkbox("Mobile Application", value=False, disabled=True)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

app_footer()