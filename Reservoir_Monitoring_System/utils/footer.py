import streamlit as st


def app_footer():

    st.divider()

    st.markdown(
        """
        <style>
        .footer{
            text-align:center;
            color:#A0A0A0;
            font-size:14px;
            line-height:1.7;
            padding-top:10px;
            padding-bottom:10px;
        }
        </style>

        <div class="footer">

        <b>Reservoir Monitoring System</b><br>

        Version <b>1.0.0</b> • Built with Python, Streamlit, Supabase & Plotly<br>

        Developed by <b>Krishna Ghute</b><br>

        © 2026 All Rights Reserved

        </div>
        """,
        unsafe_allow_html=True
    )