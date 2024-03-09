# :point_right: Week 3 Data Warehouse

This section focuses on the activities and tasks related to the data warehouse for week 3.

## Guidelines

- **Execution Environment:**
  - Ensure that this file (`web_to_gcs.py`) is run in the folder where the GCP CLI (gcli) is set up. In my case, it's located in the GCP_TERRAFORM folder within week1.

- **Script Purpose:**
  - This script is designed to download data from specified links and upload it to Google Cloud Storage (GCS). Due to discrepancies in different datasets, the script dynamically adjusts the schema for consistency. The data is uploaded in Parquet format to optimize storage and query performance.

### Scripts:

#### 1. `web_to_gcs_01.py`
   - **Description:**
     - Downloads Green Taxi data for the years 2019 and 2020 from specified links.
     - Converts the data to Parquet format with enforced datatypes.
     - Uploads the Parquet files to the designated GCS bucket.

   - **Usage:**
     - Run the script in the execution environment to perform the described tasks.

#### 2. `web_to_gcs_02.py`
   - **Description:**
     - Downloads FHV data for the year 2019 from specified links.
     - Converts the data to Parquet format with enforced datatypes.
     - Uploads the Parquet files to the designated GCS bucket.

   - **Usage:**
     - Run the script in the execution environment to perform the described tasks.

#### 3. `web_to_gcs_yellow.py`
   - **Description:**
     - Downloads Yellow Taxi data for the years 2019 and 2020 locally due to URL-related errors.
     - Converts the locally downloaded data to Parquet format with enforced datatypes.
     - Uploads the Parquet files to the designated GCS bucket.

   - **Usage:**
     - Run the script in the execution environment after downloading the Yellow Taxi data locally to perform the described tasks.

### Using this query in BigQuery

```sql
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-412810.ny_taxi.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage_testing/yellow/2019/yellow_tripdata_2019-*.parquet', 'gs://mage_testing/yellow/2020/yellow_tripdata_2020-*.parquet']
);
