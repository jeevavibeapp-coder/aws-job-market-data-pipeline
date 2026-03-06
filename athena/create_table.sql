
CREATE EXTERNAL TABLE job_market.jobs_processed (
title STRING,
company STRING,
location STRING,
skills STRING,
source STRING
)
PARTITIONED BY (year STRING, month STRING, day STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
'separatorChar'=',',
'quoteChar'='"'
)
STORED AS TEXTFILE
LOCATION 's3://job-market-processed-jeeva-de/';
