# import os
# import requests
# import pandas as pd
# from google.cloud import storage

# # Path to your GCP service account key file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\sai\Downloads\DE_Project_git_connected\DE_OLD\week1_set_up\Gcp_Terraform\keys.json"

# # Specify your GCS bucket name
# os.environ["GCP_GCS_BUCKET"] = "mage_testing"

# init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'

# def upload_to_gcs(bucket, object_name, local_file):
#     client = storage.Client()
#     bucket = client.bucket(bucket)
#     blob = bucket.blob(object_name)
#     blob.upload_from_filename(local_file)

# def web_to_gcs(year, service):
#     for i in range(12):
#         month = '0' + str(i + 1)
#         month = month[-2:]

#         file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
#         request_url = f"{init_url}{service}/{file_name}"
        
#         r = requests.get(request_url)
#         open(file_name, 'wb').write(r.content)
#         print(f"Local: {file_name}")

#         df = pd.read_csv(file_name, compression='gzip')
#         file_name = file_name.replace('.csv.gz', '.parquet')
#         df.to_parquet(file_name, engine='pyarrow')
#         print(f"Parquet: {file_name}")

#         upload_to_gcs(os.environ["GCP_GCS_BUCKET"], f"{service}/{year}/{file_name}", file_name)
#         print(f"GCS: {service}/{year}/{file_name}")

# # Customize for 'green' taxi service, years 2019 and 2020
# web_to_gcs('2019', 'green')
# web_to_gcs('2020', 'green')

# # # Customize for 'yellow' taxi service, years 2019 and 2020
# # web_to_gcs('2019', 'yellow')
# # web_to_gcs('2020', 'yellow')


### Trying if we can make the datatypes correct everywhere

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

def web_to_gcs(year, service):
    for i in range(12):
        month = '0' + str(i + 1)
        month = month[-2:]

        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        request_url = f"{init_url}{service}/{file_name}"
        
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # Define data types for specific columns
        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'ehail_fee': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'congestion_surcharge': float
        }

        # Specify columns to be parsed as datetime
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

        df = pd.read_csv(file_name, compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        
        file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(file_name, engine='pyarrow')
        print(f"Parquet: {file_name}")

        upload_to_gcs(os.environ["GCP_GCS_BUCKET"], f"{service}1/{year}/{file_name}", file_name)
        print(f"GCS: {service}/{year}/{file_name}")

# Customize for 'green' taxi service, years 2019 and 2020
web_to_gcs('2019', 'green')
web_to_gcs('2020', 'green')

# # Customize for 'yellow' taxi service, years 2019 and 2020
# web_to_gcs('2019', 'yellow')
# web_to_gcs('2020', 'yellow')
