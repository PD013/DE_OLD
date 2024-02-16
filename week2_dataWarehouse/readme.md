# :point_right: Week 3 Data Warehouse

This section focuses on the activities and tasks related to the data warehouse for week 3.

## Guidelines

- **Execution Environment:**
  - Ensure that this file (`web_to_gcs.py`) is run in the folder where the GCP CLI (gcli) is set up. In my case, it's located in the GCP_TERRAFORM folder within week1.

- **Script Purpose:**
  - This script is designed to download data from a specified link and upload it to Google Cloud Storage (GCS). Due to discrepancies in different datasets, the script dynamically adjusts the schema for consistency. The data is uploaded in Parquet format to optimize storage and query performance.

### Using this query in BigQuery

```sql
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-412810.ny_taxi.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage_testing/yellow/2019/yellow_tripdata_2019-*.parquet', 'gs://mage_testing/yellow/2020/yellow_tripdata_2020-*.parquet']
);
 
