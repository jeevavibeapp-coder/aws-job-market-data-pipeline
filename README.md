
# AWS Serverless Job Market Intelligence Pipeline

## Overview

This project implements a fully serverless data engineering pipeline on AWS that collects, processes, and analyzes Data Engineer job postings across India.

The pipeline ingests job postings from multiple APIs, stores raw data in an S3 data lake, processes the data through event-driven ETL using AWS Lambda, and enables SQL analytics using Amazon Athena.

The goal of this project is to demonstrate real-world data engineering concepts including serverless architecture, event-driven pipelines, data lake design, ETL processing, and analytics.

---

# Architecture

EventBridge → Lambda Scraper → S3 Raw → Lambda ETL → S3 Processed → Athena Analytics

## Pipeline Flow

1. EventBridge Scheduler triggers the ingestion Lambda daily.
2. Lambda Scraper fetches job postings from APIs (JSearch and LinkedIn via Apify).
3. Raw data is stored in S3 using a partitioned structure:

s3://job-market-raw-jeeva-de/
year=YYYY/month=MM/day=DD/jobs_raw.json

4. S3 Event Trigger activates the ETL Lambda when a raw file arrives.
5. Lambda ETL cleans, transforms, deduplicates, and extracts insights from job data.
6. Processed data is stored in:

s3://job-market-processed-jeeva-de/
year=YYYY/month=MM/day=DD/jobs_processed.csv

7. Amazon Athena is used to run SQL analytics on processed datasets.

---

# Tech Stack

AWS Lambda — Serverless compute for ingestion and ETL  
Amazon S3 — Data lake storage  
Amazon EventBridge — Scheduled pipeline execution  
Amazon Athena — SQL analytics  
Python — ETL logic and API integration  
REST APIs — Data ingestion (JSearch, Apify)

---

# Data Lake Structure

Raw Layer

s3://job-market-raw-jeeva-de/
year=2026/
month=02/
day=28/
jobs_raw.json

Processed Layer

s3://job-market-processed-jeeva-de/
year=2026/
month=02/
day=28/
jobs_processed.csv

---

# ETL Transformations

The ETL Lambda performs:

• HTML cleaning  
• Deduplication of job postings  
• 30‑day freshness filtering  
• Skill extraction  
• Experience parsing  
• Salary normalization

Salary fields extracted:

min_salary  
max_salary  
salary_avg  
currency

---

# Athena Table Example

CREATE EXTERNAL TABLE job_market.jobs_processed (
title STRING,
company STRING,
city STRING,
skills STRING,
experience_years INT,
min_salary INT,
max_salary INT,
salary_avg INT
)
PARTITIONED BY (year STRING, month STRING, day STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 's3://job-market-processed-jeeva-de/';

---

# Sample Analytics Queries

Total jobs processed

SELECT COUNT(*) FROM job_market.jobs_processed;

Example result: 109

---

Most demanded skills

SELECT skill, COUNT(*) AS demand
FROM job_market.jobs_processed
CROSS JOIN UNNEST(SPLIT(skills, ',')) AS t(skill)
GROUP BY skill
ORDER BY demand DESC
LIMIT 10;

---

City‑wise job distribution

SELECT city, COUNT(*) AS job_count
FROM job_market.jobs_processed
GROUP BY city
ORDER BY job_count DESC;

---

# Key Data Engineering Concepts Demonstrated

• Serverless data pipeline architecture  
• Event‑driven ETL workflows  
• Data lake design (raw and processed zones)  
• Partitioned S3 datasets  
• Schema‑on‑read analytics  
• API‑based data ingestion  
• Automated data processing  
• Deduplication logic  
• Feature engineering

---

# Scalability

The architecture scales automatically:

• Lambda auto‑scaling for ingestion  
• S3 unlimited storage  
• Athena distributed query execution  
• Event‑driven processing

---

# Cost Optimization

• Fully serverless architecture  
• No persistent compute cost  
• Athena pay‑per‑query model  
• Partitioning reduces query scan cost

---

# Future Improvements

• Skill demand trend analysis  
• Job market dashboard using Streamlit  
• Company hiring insights  
• Salary distribution analytics  
• Multi‑country job market expansion

---

# Author

Jeeva S  
Serverless Data Engineering Project – AWS Job Market Analytics
