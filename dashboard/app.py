import streamlit as st
import pandas as pd
import boto3

st.title("Data Engineer Job Market Dashboard")

# Explicitly set AWS region
region_name="ap-south-1"

# Create Athena client
athena = boto3.client(
    "athena",
   
)

st.subheader("Job Demand by City")

city_data = {
    "City": ["Bangalore", "Hyderabad", "Chennai", "Pune"],
    "Jobs": [45, 30, 20, 14]
}

city_df = pd.DataFrame(city_data)

st.bar_chart(city_df.set_index("City"))

st.subheader("Top Data Engineering Skills")

skills_data = {
    "Skill": ["Python", "SQL", "AWS", "Spark"],
    "Demand": [80, 75, 60, 40]
}

skills_df = pd.DataFrame(skills_data)

st.bar_chart(skills_df.set_index("Skill"))

st.success("Dashboard running successfully")
