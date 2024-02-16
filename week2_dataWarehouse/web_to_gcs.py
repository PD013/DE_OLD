import os
import requests
import pandas as pd
from google.cloud import storage

# Path to your GCP service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\sai\Downloads\DE_Project_git_connected\DE_OLD\week1_set_up\Gcp_Terraform\keys.json"

# Specify your GCS bucket name
os.environ["GCP_GCS_BUCKET"] = "mage_testing"

init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'

def upload_to_gcs(bucket, object_name, local_file):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)

def enforce_data_types(df):
    # Enforce data types for columns
    df = df.astype({
        "VendorID": "Int64",
        "tpep_pickup_datetime": "datetime64[ns]",
        "tpep_dropoff_datetime": "datetime64[ns]",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "bool",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    })
    return df

def web_to_gcs(year, service):
    for i in range(12):
        month = '0' + str(i + 1)
        month = month[-2:]

        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        request_url = f"{init_url}{service}/{file_name}"
        
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        df = pd.read_csv(file_name, compression='gzip')
        df = enforce_data_types(df)

        parquet_file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(parquet_file_name, engine='pyarrow')
        print(f"Parquet: {parquet_file_name}")

        upload_to_gcs(os.environ["GCP_GCS_BUCKET"], f"{service}/{year}/{parquet_file_name}", parquet_file_name)
        print(f"GCS: {service}/{year}/{parquet_file_name}")

# # Customize for 'green' taxi service, years 2019 and 2020
# web_to_gcs('2019', 'green')
# web_to_gcs('2020', 'green')

# Customize for 'yellow' taxi service, years 2019 and 2020
web_to_gcs('2019', 'yellow')
web_to_gcs('2020', 'yellow')
