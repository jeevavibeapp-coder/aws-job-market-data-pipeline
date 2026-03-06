
import json
import boto3
import csv
from io import StringIO

s3 = boto3.client("s3")

RAW_BUCKET = "job-market-raw-jeeva-de"
PROCESSED_BUCKET = "job-market-processed-jeeva-de"

def lambda_handler(event, context):

    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]

    obj = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(obj["Body"].read())

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "title","company","location","skills","source"
    ])

    for job in data:
        title = job.get("job_title")
        company = job.get("employer_name")
        location = job.get("job_city")
        skills = ""
        source = "jsearch"

        writer.writerow([title,company,location,skills,source])

    processed_key = key.replace("raw","processed").replace(".json",".csv")

    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        Key=processed_key,
        Body=output.getvalue()
    )

    return {
        "status":"success",
        "records_processed":len(data)
    }
