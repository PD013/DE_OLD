# This is for fhv file upload from the link 
# datatype forcing is not done in this 


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

        df = pd.read_csv(file_name, compression='gzip')
        file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(file_name, engine='pyarrow')
        print(f"Parquet: {file_name}")

        upload_to_gcs(os.environ["GCP_GCS_BUCKET"], f"{service}/{year}/{file_name}", file_name)
        print(f"GCS: {service}/{year}/{file_name}")


web_to_gcs('2019', 'fhv')

