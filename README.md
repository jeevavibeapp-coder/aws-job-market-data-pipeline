
# AWS Serverless Job Market Intelligence Pipeline

## Overview
Serverless data engineering project that collects, processes, and analyzes Data Engineer job postings across India.

## Architecture
EventBridge → Lambda Scraper → S3 Raw → Lambda ETL → S3 Processed → Athena Analytics

## Tech Stack
- AWS Lambda
- Amazon S3
- Amazon EventBridge
- Amazon Athena
- Python
- REST APIs

## Features
- Multi-source job ingestion
- Event-driven ETL
- Partitioned S3 data lake
- Deduplication & filtering
- Skill extraction
- Salary normalization
- Athena analytics

## Example Query

Top skills demand

SELECT skill, COUNT(*)
FROM job_market.jobs_processed
CROSS JOIN UNNEST(SPLIT(skills, ',')) AS t(skill)
GROUP BY skill
ORDER BY COUNT(*) DESC;
