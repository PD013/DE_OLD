# NY Taxi Data Analysis

This repository contains SQL queries and analysis for processing New York taxi data.

---

## Question 1: Creating materialized table from external table 

```sql
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-412810.ny_taxi.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage_testing/green_taxi/*']
);
``` 

## Creating a materialized table from external table 
```sql
CREATE OR REPLACE TABLE dtc-de-course-412810.ny_taxi.materialized_green_tripdata
AS (
 SELECT * FROM `dtc-de-course-412810.ny_taxi.external_green_tripdata`
);
```

## Count Total Data Question 1 = 840402
```sql
SELECT COUNT(*) FROM `dtc-de-course-412810.ny_taxi.external_green_tripdata`;
```

## Question 2 
-- Takes 0B to run
```sql
SELECT COUNT(DISTINCT PULocationID) FROM `dtc-de-course-412810.ny_taxi.external_green_tripdata`;
```
-- Takes 6.4 Mb to run
```sql
SELECT COUNT(DISTINCT PULocationID) FROM `dtc-de-course-412810.ny_taxi.materialized_green_tripdata`;
```

## Question 3
-- Answer - 1622
```sql
SELECT COUNT(fare_amount) FROM `dtc-de-course-412810.ny_taxi.materialized_green_tripdata` WHERE fare_amount = 0;
```

## Question 4
-- Create a partitioned and clustered table from external table
```sql
CREATE OR REPLACE TABLE dtc-de-course-412810.ny_taxi.green_tripdata_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM dtc-de-course-412810.ny_taxi.materialized_green_tripdata;
```

## Question 5
-- 12.82 MB
```sql
SELECT DISTINCT PULocationID FROM ny_taxi.materialized_green_tripdata
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
```

-- 1.12 MB
```sql
SELECT DISTINCT PULocationID FROM ny_taxi.green_tripdata_partitoned_clustered
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
```

## Question 6 
-- Data of External table is stored in ```Gcp Bucket```

## Question 7 
```False``` Cause its not alaways good to do partitioning it depends on data size and need

## Question 8
```sql
SELECT COUNT(*) FROM ny_taxi.materialized_green_tripdata;
```


