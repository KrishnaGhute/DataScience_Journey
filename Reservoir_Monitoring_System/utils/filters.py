import streamlit as st
import pandas as pd


def global_date_filter(df):
    """
    Displays global date filters and returns the filtered dataframe.
    """

    df = df.copy()
    df["record_date"] = pd.to_datetime(df["record_date"])

    min_date = df["record_date"].min().date()
    max_date = df["record_date"].max().date()

    st.markdown("## 📅 Data Filters")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        start_date = st.date_input(
            "Start Date",
            value=min_date,
            min_value=min_date,
            max_value=max_date,
        )

    with col2:
        end_date = st.date_input(
            "End Date",
            value=max_date,
            min_value=min_date,
            max_value=max_date,
        )

    with col3:
        st.markdown("<br>", unsafe_allow_html=True)

        quick = st.selectbox(
            "Quick Filter",
            [
                "Custom",
                "Last 30 Days",
                "Last 90 Days",
                "Last 6 Months",
                "Last 1 Year",
                "All Data",
            ],
        )

    if quick != "Custom":

        latest = df["record_date"].max()

        if quick == "Last 30 Days":
            start_date = (latest - pd.Timedelta(days=30)).date()

        elif quick == "Last 90 Days":
            start_date = (latest - pd.Timedelta(days=90)).date()

        elif quick == "Last 6 Months":
            start_date = (latest - pd.DateOffset(months=6)).date()

        elif quick == "Last 1 Year":
            start_date = (latest - pd.DateOffset(years=1)).date()

        elif quick == "All Data":
            start_date = min_date

        end_date = latest.date()

    filtered = df[
        (df["record_date"] >= pd.Timestamp(start_date))
        & (df["record_date"] <= pd.Timestamp(end_date))
    ]

    return filtered