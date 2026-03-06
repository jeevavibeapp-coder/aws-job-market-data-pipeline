import streamlit as st
import pandas as pd

st.title("Data Engineer Job Market Dashboard")

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
