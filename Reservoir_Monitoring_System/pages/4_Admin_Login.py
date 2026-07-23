# ==========================================================
# pages/4_Admin_Login.py
# ==========================================================

import streamlit as st
from utils.database import supabase

from utils.footer import app_footer

from utils.sidebar import app_sidebar

from admin.panel import show_admin_panel

st.set_page_config(
    page_title="Admin Login",
    page_icon="🔐",
    layout="centered"
)

app_sidebar()

# ==========================================================
# SESSION
# ==========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ==========================================================
# IF NOT LOGGED IN
# ==========================================================

if not st.session_state.logged_in:

    st.title("🔐 Administrator Login")

    st.caption(
        "Authorized personnel only. Enter your administrator credentials."
    )

    with st.form("admin_login"):

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        login = st.form_submit_button(
            "Login",
            use_container_width=True
        )

        if login:

            if username == "" or password == "":

                st.warning(
                    "Please enter both username and password."
                )

            else:

                try:

                    response = (
                        supabase
                        .table("admin_users")
                        .select("*")
                        .eq("username", username.strip())
                        .execute()
                    )

                    if len(response.data) == 0:

                        st.error(
                            "❌ Invalid administrator username or password."
                        )

                    else:

                        user = response.data[0]

                        if str(user["password_hash"]).strip() == password.strip():

                            st.session_state.logged_in = True
                            st.session_state.username = username

                            st.success("✅ Login Successful")

                            st.rerun()

                        else:

                            st.error(
                                "❌ Invalid administrator username or password."
                            )

                except Exception:

                    st.error(
                        "Unable to connect to the authentication server."
                    )
                    

# ==========================================================
# ADMIN PANEL
# ==========================================================

else:

    show_admin_panel()
    
    
app_footer()