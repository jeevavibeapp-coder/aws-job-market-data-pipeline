
import json
import os
import requests
import boto3
from datetime import datetime

s3 = boto3.client("s3")

RAW_BUCKET = os.environ.get("RAW_BUCKET")
JSEARCH_KEY = os.environ.get("JSEARCH_KEY")
APIFY_TOKEN = os.environ.get("APIFY_TOKEN")

def fetch_jsearch():
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": JSEARCH_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": "data engineer india",
        "page": "1",
        "num_pages": "1"
    }
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        return r.json().get("data", [])
    return []

def lambda_handler(event, context):
    jobs = fetch_jsearch()

    now = datetime.utcnow()
    key = f"year={now.year}/month={now.month}/day={now.day}/jobs_raw.json"

    s3.put_object(
        Bucket=RAW_BUCKET,
        Key=key,
        Body=json.dumps(jobs)
    )

    return {
        "status": "success",
        "records_fetched": len(jobs)
    }
