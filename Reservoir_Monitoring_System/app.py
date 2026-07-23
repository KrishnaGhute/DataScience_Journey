import streamlit as st
from utils.database import test_connection, get_all_dams, get_latest_records
from utils.styles import load_styles

from utils.footer import app_footer

from utils.sidebar import app_sidebar

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Reservoir Intelligence Platform",
    page_icon="💧",
    layout="wide"
)

app_sidebar()

load_styles()

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}


.hero {

    padding: 35px;
    border-radius: 20px;
    background:
    linear-gradient(135deg,#0F2027,#203A43,#2C5364);

}


.hero h1 {

    color:white;
    font-size:45px;

}


.hero p {

    color:#d7e9ff;
    font-size:18px;

}



.card {

    background:#161B22;
    padding:25px;
    border-radius:15px;
    border:1px solid #30363d;

}


.card h3 {

    color:white;

}


.card p {

    color:#c9d1d9;

}


.card li {
    color: white;
    font-size: 16px;
    line-height: 1.8;
}


.footer {

    text-align:center;
    color:#8b949e;
    padding:20px;

}


</style>
""", unsafe_allow_html=True)



# =====================================================
# DATABASE
# =====================================================

status = test_connection()

dams = get_all_dams()
records = get_latest_records()


total_dams = len(dams)
total_records = len(records)



# =====================================================
# HERO SECTION
# =====================================================


st.markdown("""
<div class="hero">

<h1>💧 Reservoir Intelligence Platform</h1>

<p>
A cloud-based water resource monitoring and analytics system
for tracking reservoir storage, inflow, outflow and operational insights.
</p>

</div>

""", unsafe_allow_html=True)



st.write("")


# =====================================================
# STATUS
# =====================================================

if status is True:

    st.success(
        "🟢 System Online | Connected with Cloud Database"
    )

else:

    st.error(status)



# =====================================================
# KPI SECTION
# =====================================================


st.subheader("📊 System Overview")


c1,c2,c3,c4 = st.columns(4)


with c1:

    st.metric(
        "🏞 Reservoirs",
        total_dams
    )


with c2:

    st.metric(
        "📚 Data Records",
        f"{total_records:,}"
    )


with c3:

    st.metric(
        "☁ Cloud Status",
        "Active"
    )


with c4:

    st.metric(
        "📈 Analytics",
        "Enabled"
    )



st.divider()



# =====================================================
# ABOUT
# =====================================================


st.header("🌊 Platform Overview")


st.markdown("""
<div class="card">

<h3>Reservoir Monitoring & Analytics Engine</h3>


<p>

This platform provides centralized reservoir data management,
interactive visualization and operational monitoring.

The system enables users to analyze:

</p>


<ul>

<li>Current reservoir storage levels</li>

<li>Historical storage trends</li>

<li>Water inflow and outflow patterns</li>

<li>Capacity utilization</li>

<li>Geographical reservoir distribution</li>

</ul>


</div>

""",unsafe_allow_html=True)



st.write("")



# =====================================================
# FEATURES
# =====================================================


st.header("🚀 Core Capabilities")


features = [

("🗺 Interactive Map",
"Visualize reservoir locations with live status information"),

("📈 Historical Analytics",
"Analyze storage trends and water availability"),

("☁ Cloud Database",
"Secure online reservoir data storage"),

("⚙ Admin Management",
"Upload and manage reservoir observations"),

("📊 Data Exploration",
"Interactive Plotly based analytics"),

("📥 Export System",
"Download processed reservoir datasets")

]


cols = st.columns(3)


for i,(title,desc) in enumerate(features):

    with cols[i%3]:

        st.markdown(f"""

        <div class="card">

        <h3>{title}</h3>

        <p>{desc}</p>

        </div>

        """,
        unsafe_allow_html=True
        )



st.write("")

st.divider()



# =====================================================
# TECHNOLOGY STACK
# =====================================================


st.header("🛠 Technology Architecture")


a,b,c,d = st.columns(4)


a.info("🐍 Python\n\nData Processing")

b.info("📊 Streamlit\n\nDashboard")

c.info("☁ Supabase\n\nCloud Database")

d.info("📈 Plotly\n\nVisualization")



st.divider()



# =====================================================
# PROJECT VALUE
# =====================================================


st.header("🎯 Project Objective")


st.write("""
The goal of this system is to transform raw reservoir observations
into meaningful operational intelligence through data engineering,
visual analytics and cloud-based monitoring.
""")


app_footer()