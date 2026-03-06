import streamlit as st
import boto3
import pandas as pd
import time

AWS_REGION = "ap-south-1"
DATABASE = "job_market"
OUTPUT = "s3://aws-athena-query-results-jeeva/"

athena = boto3.client("athena", region_name=AWS_REGION)

def run_query(query):

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": OUTPUT},
    )

    query_execution_id = response["QueryExecutionId"]

    while True:
        status = athena.get_query_execution(QueryExecutionId=query_execution_id)

        state = status["QueryExecution"]["Status"]["State"]

        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break

        time.sleep(1)

    results = athena.get_query_results(QueryExecutionId=query_execution_id)

    rows = results["ResultSet"]["Rows"]

    data = []

    for row in rows[1:]:
        data.append([col.get("VarCharValue") for col in row["Data"]])

    columns = [col["VarCharValue"] for col in rows[0]["Data"]]

    return pd.DataFrame(data, columns=columns)


st.title("Data Engineer Job Market Dashboard")

st.header("Total Jobs Collected")

query = """
SELECT count(*) as total_jobs
FROM jobs_processed
"""

df = run_query(query)

st.metric("Jobs collected", df.iloc[0][0])


st.header("Top Skills Demand")

query = """
SELECT skills, count(*) as demand
FROM jobs_processed
GROUP BY skills
ORDER BY demand DESC
LIMIT 10
"""

df = run_query(query)

st.bar_chart(df.set_index("skills"))


st.header("Experience Level Demand")

query = """
SELECT experience_years, count(*) as jobs
FROM jobs_processed
GROUP BY experience_years
ORDER BY experience_years
"""

df = run_query(query)

st.bar_chart(df.set_index("experience_years"))
