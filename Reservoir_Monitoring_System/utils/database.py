# ==========================================================
# utils/database.py
# Reservoir Monitoring System
# Database Operations using Supabase
# ==========================================================

import streamlit as st
from supabase import create_client

# ==========================================================
# SUPABASE CONNECTION
# ==========================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==========================================================
# CONNECTION TEST
# ==========================================================

def test_connection():
    try:
        supabase.table("dams").select("*").limit(1).execute()
        return True
    except Exception as e:
        return str(e)


# ==========================================================
# ADMIN LOGIN
# ==========================================================

def verify_admin(username, password):

    try:

        response = (
            supabase
            .table("admin_users")
            .select("*")
            .eq("username", username)
            .execute()
        )

        if len(response.data) == 0:
            return False

        user = response.data[0]

        if user["password_hash"] == password:
            return True

        return False

    except:
        return False


# ==========================================================
# ALL DAMS
# ==========================================================

def get_all_dams():
    try:
        response = (
            supabase
            .table("dams")
            .select("*")
            .order("dam_name")
            .execute()
        )
        return response.data

    except Exception as e:
        st.error(f"Error fetching dams: {e}")
        return []


def get_dam(dam_id):

    try:

        response = (
            supabase
            .table("dams")
            .select("*")
            .eq("dam_id", dam_id)
            .execute()
        )

        if response.data:

            return response.data[0]

        return None

    except Exception as e:

        st.error(e)

        return None


# ==========================================================
# DAILY RECORDS
# ==========================================================

def get_dam_data(dam_id):

    try:

        response = (
            supabase
            .table("daily_records")
            .select("*")
            .eq("dam_id", dam_id)
            .order("record_date")
            .execute()
        )

        return response.data

    except Exception as e:

        st.error(e)

        return []


# ==========================================================
# GET LATEST RECORD OF EACH DAM
# ==========================================================

def get_latest_records():
    try:
        response = (
            supabase
            .table("latest_daily_records")
            .select("*")
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Error fetching latest records: {e}")
        return []


# ==========================================================
# INSERT
# ==========================================================

def insert_daily_record(payload):

    try:

        supabase.table("daily_records").insert(payload).execute()

        return True, "Inserted Successfully"

    except Exception as e:

        return False, str(e)


# ==========================================================
# UPDATE
# ==========================================================

def update_daily_record(record_id, payload):

    try:

        supabase.table("daily_records") \
            .update(payload) \
            .eq("record_id", record_id) \
            .execute()

        return True

    except Exception as e:

        st.error(e)

        return False


# ==========================================================
# DELETE
# ==========================================================

def delete_daily_record(record_id):

    try:

        supabase.table("daily_records") \
            .delete() \
            .eq("record_id", record_id) \
            .execute()

        return True

    except Exception as e:

        st.error(e)

        return False


# ==========================================================
# SEARCH
# ==========================================================

def search_records(dam_id, start_date, end_date):

    try:

        response = (

            supabase

            .table("daily_records")

            .select("*")

            .eq("dam_id", dam_id)

            .gte("record_date", str(start_date))

            .lte("record_date", str(end_date))

            .order("record_date")

            .execute()

        )

        return response.data

    except Exception as e:

        st.error(e)

        return []


# ==========================================================
# DASHBOARD DATA
# ==========================================================

def get_latest_records():
    try:
        response = (
            supabase
            .table("latest_daily_records")
            .select("*")
            .execute()
        )
        return response.data
    except Exception as e:
        st.error(f"Error fetching latest records: {e}")
        return []


# ==========================================================
# ALL DAMS
# ==========================================================

def get_all_dams():
    try:
        response = (
            supabase
            .table("dams")
            .select("*")
            .order("dam_name")
            .execute()
        )
        return response.data
    except Exception as e:
        st.error(f"Error fetching dams: {e}")
        return []


# ==========================================================
# HISTORY OF A SINGLE DAM
# ==========================================================

# ==========================================================
# GET HISTORY OF SINGLE DAM
# ==========================================================

def get_dam_history(dam_id, start_date=None, end_date=None):

    try:

        query = (
            supabase
            .table("dam_history")
            .select("*")
            .eq("dam_id", dam_id)
        )

        if start_date:
            query = query.gte("record_date", str(start_date))

        if end_date:
            query = query.lte("record_date", str(end_date))

        response = (
            query
            .order("record_date")
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Database Error : {e}")
        return []
    
    
# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

def get_dashboard_summary():
    try:
        response = (
            supabase
            .table("dashboard_summary")
            .select("*")
            .execute()
        )

        if response.data:
            return response.data[0]

        return {}

    except Exception as e:
        st.error(f"Dashboard summary error: {e}")
        return {}

# ==========================================================
# TOTAL COUNTS
# ==========================================================

def total_dams():

    return len(get_all_dams())


def total_records():

    try:

        response = (
            supabase
            .table("daily_records")
            .select("*", count="exact")
            .limit(1)
            .execute()
        )

        return response.count

    except Exception:

        return 0

# ==========================================================
# GET LATEST RECORD OF EACH DAM
# ==========================================================

def get_latest_records():
    try:
        response = (
            supabase
            .table("latest_daily_records")
            .select("*")
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Error fetching latest records: {e}")
        return []
    
    
    
    
# ==========================================================
# get history of single dam
# ==========================================================
def get_dam_history(dam_id, start_date=None, end_date=None):

    try:

        query = (
            supabase
            .table("dam_history")
            .select("*")
            .eq("dam_id", dam_id)
        )

        if start_date:
            query = query.gte("record_date", str(start_date))

        if end_date:
            query = query.lte("record_date", str(end_date))

        response = (
            query
            .order("record_date")
            .execute()
        )

        return response.data

    except Exception as e:
        st.error(f"Database Error : {e}")
        return []