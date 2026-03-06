import streamlit as st
import pandas as pd
import boto3

st.title("Data Engineer Job Market Dashboard")

athena = boto3.client("athena")

query = """
SELECT city, COUNT(*) as jobs
FROM job_market.jobs_processed
GROUP BY city
ORDER BY jobs DESC
LIMIT 10
"""

st.write("Top Cities for Data Engineer Jobs")

st.code(query)

st.info("Run this query in Athena to visualize job distribution.")

data = {
    "City": ["Bangalore","Hyderabad","Chennai","Pune"],
    "Jobs": [45,30,20,14]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("City"))
