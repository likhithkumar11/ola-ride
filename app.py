import streamlit as st

# Page config
st.set_page_config(
    page_title="OLA Ride Analytics",
    layout="wide"
)

# Title
st.title("🚕 OLA Ride Analytics Dashboard")
st.markdown(
    "This Streamlit application presents key insights derived from SQL analysis and Power BI dashboards."
)

# KPI Section
st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rides", "103K")
col2.metric("Successful Rides", "64K")
col3.metric("Total Revenue", "₹57M")

# Interactive Filter
st.subheader("🔍 Interactive Filter")

vehicle_type = st.selectbox(
    "Select Vehicle Type",
    ["All", "Prime Sedan", "Mini", "Auto", "Bike", "Prime SUV"]
)

st.write(f"Showing insights for: **{vehicle_type}**")

# Insights Section
st.subheader("📈 Key Insights")

st.write("""
- Prime Sedan contributes the highest ride distance  
- UPI and Cash dominate payment methods  
- Driver-related issues are the leading cause of cancellations  
- Customer and driver ratings average around 4, indicating stable service quality  
""")

# SQL Reference
st.subheader("🗄 Data Source")
st.write(
    "Insights presented in this application are generated using SQL queries on OLA ride booking data."
)
