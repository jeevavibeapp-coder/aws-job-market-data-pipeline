import streamlit as st
import pandas as pd
import boto3

st.title("Data Engineer Job Market Dashboard")

# AWS Athena client with region
athena = boto3.client(
    "athena",
    region_name="ap-south-1"
)

st.subheader("Sample Insights")

data = {
    "City": ["Bangalore", "Hyderabad", "Chennai", "Pune"],
    "Jobs": [45, 30, 20, 14]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("City"))

st.subheader("Top Skills")

skills = {
    "Skill": ["Python", "SQL", "AWS", "Spark"],
    "Demand": [80, 75, 60, 40]
}

skills_df = pd.DataFrame(skills)

st.bar_chart(skills_df.set_index("Skill"))
