# =====================================================
# utils/styles.py
# Global Streamlit Styling
# =====================================================


import streamlit as st


def load_styles():

    st.markdown("""

    <style>

    /* Main Background */

    .main {
        background-color: #0E1117;
    }


    /* Hero Section */

    .hero {

        padding:35px;
        border-radius:20px;

        background:
        linear-gradient(
        135deg,
        #0F2027,
        #203A43,
        #2C5364
        );

    }


    .hero h1 {

        color:white;
        font-size:45px;

    }


    .hero p {

        color:#d7e9ff;
        font-size:18px;

    }



    /* Cards */


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

        color:#d7e9ff;

    }


    .card li {

        color:white;

        line-height:1.8;

    }



    /* Headers */

    h1,h2,h3 {

        color:white;

    }



    /* Metric cards */

    div[data-testid="metric-container"] {

        background:#161B22;

        padding:20px;

        border-radius:15px;

        border:1px solid #30363d;

    }



    /* Footer */

    .footer {

        text-align:center;

        color:#8b949e;

        padding:20px;

    }



    </style>


    """,
    unsafe_allow_html=True
    )
    
    
    