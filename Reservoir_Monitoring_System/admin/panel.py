# ==========================================================
# IMPORTS
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

from utils.database import (
    get_all_dams,
    insert_daily_record,
    supabase
)

from utils.footer import app_footer

from utils.sidebar import app_sidebar

app_sidebar()

def show_admin_panel():
    # ==========================================================
    # HEADER
    # ==========================================================

    st.title("🛠 Administrator Control Center")

    st.caption(
        "Secure interface for managing reservoir information, historical observations, and system datasets."
    )

    st.divider()

    left, right = st.columns([5, 1])

    with left:

        st.success(
            f"Logged in as **{st.session_state.username}**"
        )

    with right:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()

    st.divider()

    # ==========================================================
    # DATABASE SUMMARY
    # ==========================================================

    dams = get_all_dams()

    total_dams = len(dams)

    try:

        response = (
            supabase
            .table("daily_records")
            .select("*", count="exact")
            .limit(1)
            .execute()
        )

        total_records = response.count or 0

    except:

        total_records = 0

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🏞 Registered Reservoirs",
        total_dams
    )

    c2.metric(
        "📄 Historical Records",
        f"{total_records:,}"
    )

    c3.metric(
        "👤 Active Administrator",
        st.session_state.username
    )

    st.divider()

    # ==========================================================
    # TABS
    # ==========================================================

    tab1, tab2, tab3 = st.tabs([
        "📝 Daily Record Entry",
        "📤 Bulk Dataset Migration",
        "🗂 Reservoir Database"
    ])

    # --- TAB 1: SINGLE DATA ENTRY ---
    with tab1:

        st.subheader("📝 Daily Reservoir Observation Entry")

        st.caption(
            "Record the latest hydrological observations for an individual reservoir."
        )

        st.divider()

        dams = get_all_dams()

        if not dams:

            st.info(
                "No reservoirs found in the database. Please perform a bulk migration first."
            )

        else:

            dam_options = {
                dam["dam_name"]: dam
                for dam in dams
            }

            selected_dam_name = st.selectbox(
                "🏞 Select Reservoir",
                list(dam_options.keys())
            )

            selected_dam = dam_options[selected_dam_name]

            # --------------------------------------------------
            # Reservoir Information
            # --------------------------------------------------

            info1, info2, info3 = st.columns(3)

            info1.metric(
                "Full Capacity",
                f"{selected_dam['full_capacity']:,.0f} MCFT"
            )

            info2.metric(
                "Maximum Depth",
                f"{selected_dam['full_depth']:.2f} ft"
            )

            info3.metric(
                "Reservoir ID",
                selected_dam["dam_id"]
            )

            st.divider()

            with st.form(
                "daily_record_form",
                clear_on_submit=True
            ):

                st.markdown("### 📅 Observation Details")

                c1, c2 = st.columns(2)

                with c1:

                    record_date = st.date_input(
                        "Observation Date",
                        date.today()
                    )

                    current_level = st.number_input(
                        "Current Water Level (ft)",
                        min_value=0.0,
                        step=0.1
                    )

                    current_storage = st.number_input(
                        "Current Storage (MCFT)",
                        min_value=0.0,
                        step=0.1
                    )

                with c2:

                    current_inflow = st.number_input(
                        "Daily Inflow (MCFT/day)",
                        min_value=0.0,
                        step=0.1
                    )

                    current_outflow = st.number_input(
                        "Daily Outflow (MCFT/day)",
                        min_value=0.0,
                        step=0.1
                    )

                st.markdown("### 📝 Additional Notes")

                remarks = st.text_area(
                    "Remarks",
                    placeholder="Maintenance, rainfall, gate operations, inspection notes..."
                )

                st.divider()

                submit_btn = st.form_submit_button(
                    "💾 Save Observation",
                    use_container_width=True
                )

                if submit_btn:

                    full_capacity = selected_dam["full_capacity"]

                    storage_pct = (
                        current_storage /
                        full_capacity
                    ) * 100 if full_capacity else 0

                    net_flow = (
                        current_inflow -
                        current_outflow
                    )

                    payload = {

                        "dam_id": selected_dam["dam_id"],

                        "record_date": str(record_date),

                        "current_level": current_level,

                        "current_storage": current_storage,

                        "current_inflow": current_inflow,

                        "current_outflow": current_outflow,

                        "storage_pct": round(storage_pct, 2),

                        "net_flow": net_flow,

                        "remarks": remarks

                    }

                    success, error_msg = insert_daily_record(payload)

                    if success:

                        st.success(
                            f"✅ Observation successfully recorded for {selected_dam_name}."
                        )

                    else:

                        st.error(error_msg)

    # --- TAB 2: BULK CSV UPLOAD ---
    with tab2:

        st.subheader("📤 Historical Dataset Migration")

        st.caption(
            "Import historical reservoir observations from a CSV dataset into the cloud database."
        )

        st.divider()

        st.info("""
    ### Supported Dataset

    The uploaded CSV should contain:

    - Reservoir Name
    - Observation Date
    - Water Level
    - Storage
    - Inflow
    - Outflow
    - Capacity Percentage
    - Net Flow
    - Coordinates
    - Reservoir Capacity
    """)

        uploaded_file = st.file_uploader(
            "Choose Reservoir Dataset (.csv)",
            type=["csv"]
        )

        if uploaded_file is not None:

            try:

                df = pd.read_csv(uploaded_file)

                st.success(
                    f"Dataset loaded successfully ({len(df):,} records)"
                )

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Rows",
                    f"{len(df):,}"
                )

                c2.metric(
                    "Columns",
                    len(df.columns)
                )

                c3.metric(
                    "Reservoirs",
                    df["dam_name"].nunique()
                )

                with st.expander("Dataset Preview"):

                    st.dataframe(
                        df.head(10),
                        use_container_width=True
                    )

                st.divider()

                if st.button(
                    "🚀 Start Migration",
                    use_container_width=True,
                    type="primary"
                ):

                    progress = st.progress(0)

                    status = st.empty()

                    # ----------------------------------------

                    status.info(
                        "Step 1/4 : Reading Dataset..."
                    )

                    df = df.replace(
                        {np.nan: None}
                    )

                    progress.progress(20)

                    # ----------------------------------------

                    status.info(
                        "Step 2/4 : Registering Reservoirs..."
                    )

                    unique_dams = df[
                        [
                            "dam_name",
                            "latitude",
                            "longitude",
                            "full_capacity",
                            "full_depth"
                        ]
                    ].drop_duplicates(
                        subset=["dam_name"]
                    )

                    for _, row in unique_dams.iterrows():

                        supabase.table("dams").upsert(

                            {

                                "dam_name": row["dam_name"],

                                "latitude": row["latitude"],

                                "longitude": row["longitude"],

                                "full_capacity": row["full_capacity"],

                                "full_depth": row["full_depth"]

                            },

                            on_conflict="dam_name"

                        ).execute()

                    progress.progress(45)

                    # ----------------------------------------

                    status.info(
                        "Step 3/4 : Preparing Historical Records..."
                    )

                    dams_response = (
                        supabase
                        .table("dams")
                        .select("dam_id, dam_name")
                        .execute()
                    )

                    dam_lookup = {

                        d["dam_name"]: d["dam_id"]

                        for d in dams_response.data

                    }

                    df["dam_id"] = df["dam_name"].map(dam_lookup)

                    df = df.dropna(subset=["dam_id"])

                    records = []

                    for _, row in df.iterrows():

                        records.append({

                            "dam_id": int(row["dam_id"]),

                            "record_date": str(row["date"]).split(" ")[0],

                            "current_level": row["current_level"],

                            "current_storage": row["current_storage"],

                            "current_inflow": row["current_inflow"],

                            "current_outflow": row["current_outflow"],

                            "storage_pct": round(row["storage_pct"],2),

                            "net_flow": row["net_flow"],

                            "remarks": f"Bulk Upload | {row.get('season','N/A')}"

                        })

                    progress.progress(70)

                    # ----------------------------------------

                    status.info(
                        "Step 4/4 : Uploading Records..."
                    )

                    batch_size = 500

                    for i in range(0, len(records), batch_size):

                        supabase.table(

                            "daily_records"

                        ).insert(

                            records[i:i+batch_size]

                        ).execute()

                    progress.progress(100)

                    status.success(
                        "Migration Completed Successfully."
                    )

                    st.success("""
    ### ✅ Migration Summary

    The historical dataset has been uploaded successfully.

    Reservoir information has been synchronized.

    Daily observations are now available for analysis and forecasting.

    The dashboard is ready for use.
    """)

                    st.balloons()

            except Exception as e:

                st.error(
                    f"Migration failed.\n\n{e}"
                )
                
    # ==========================================================
    # TAB 3
    # RESERVOIR DATABASE
    # ==========================================================

    # ==========================================================
    # TAB 3 : RESERVOIR DATABASE
    # ==========================================================

    with tab3:

        st.subheader("🗂 Reservoir Database")

        st.caption(
            "View all registered reservoirs stored in the system."
        )

        st.divider()

        dams = get_all_dams()

        if not dams:

            st.warning("No reservoirs found.")

        else:

            df_dams = pd.DataFrame(dams)

            search = st.text_input(
                "🔍 Search Reservoir"
            )

            if search:

                df_dams = df_dams[
                    df_dams["dam_name"]
                    .str.contains(search, case=False)
                ]

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Reservoirs",
                len(df_dams)
            )

            c2.metric(
                "Average Capacity",
                f"{df_dams['full_capacity'].mean():,.0f} MCFT"
            )

            c3.metric(
                "Maximum Depth",
                f"{df_dams['full_depth'].max():.2f} ft"
            )

            st.divider()

            st.dataframe(

                df_dams[[
                    "dam_id",
                    "dam_name",
                    "full_capacity",
                    "full_depth",
                    "latitude",
                    "longitude"
                ]],

                use_container_width=True,

                hide_index=True

            )
            
            
    app_footer()