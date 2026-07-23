import streamlit as st

def app_sidebar():

    with st.sidebar:

        # ----------------------------------
        # LOGO
        # ----------------------------------

        st.image(
            "assets/logo.png",
            width=80
        )

        # ----------------------------------
        # APP TITLE
        # ----------------------------------

        st.markdown(
            """
            <div style='padding-top:5px; padding-bottom:5px;'>
                <h2 style='margin-bottom:0px;'>Reservoir Monitoring System</h2>
                <span style='color:#9CA3AF; font-size:13px;'>Version 1.0.0</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # ----------------------------------
        # SYSTEM STATUS
        # ----------------------------------

        st.markdown(
            """
            <div style='padding:8px 0;'>
                <span style='color:#22C55E; font-weight:600;'>🟢 System Online</span><br>
                <span style='color:#9CA3AF; font-size:12px;'>Supabase connected</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # ----------------------------------
        # QUICK INFO
        # ----------------------------------

        st.markdown(
            """
            **📊 Quick Info**

            • 19 Reservoirs

            • 55,500 Records

            • 2018–2025 Dataset

            • Real-time Dashboard
            """
        )

        st.divider()

        # ----------------------------------
        # DEVELOPER
        # ----------------------------------

        st.markdown(
            """
            <div style='padding-top:5px;'>
                <span style='color:#9CA3AF; font-size:12px;'>Developed by</span><br>
                <b>Krishna Ghute</b><br>
                <span style='color:#9CA3AF; font-size:12px;'>Data Science Professional</span>
            </div>
            """,
            unsafe_allow_html=True
        )