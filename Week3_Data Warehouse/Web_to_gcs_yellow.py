# THIS WAS USED FOR YELLOW DATA DOWNLOAD AND Due to error in yellow_data we have downloaded it locally and 
# then used this code 

# Difference in both is the datatype forcing when uploading


# import os
# import pandas as pd
# from google.cloud import storage

# # Path to your GCP service account key file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\sai\Downloads\DE_Project_git_connected\DE_OLD\week1_set_up\Gcp_Terraform\keys.json"

# # Specify your GCS bucket name
# os.environ["GCP_GCS_BUCKET"] = "mage_testing"

# def upload_to_gcs(bucket, object_name, local_file):
#     client = storage.Client()
#     bucket = client.bucket(bucket)
#     blob = bucket.blob(object_name)
#     blob.upload_from_filename(local_file)

# def process_and_upload(local_file_path, gcs_object_path):
#     try:
#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(local_file_path)

#         # Convert DataFrame to Parquet format using pyarrow
#         parquet_file_path = local_file_path.replace('.csv', '.parquet')
#         df.to_parquet(parquet_file_path, engine='pyarrow')

#         # Upload the Parquet file to GCS
#         upload_to_gcs(os.environ["GCP_GCS_BUCKET"], gcs_object_path, parquet_file_path)

#         print(f"Parquet file '{parquet_file_path}' uploaded to GCS as '{gcs_object_path}'")

#     except Exception as e:
#         print(f"Error processing {local_file_path}: {e}")

# # FOR 2019 Files after downloading them in the system
# # Example usage for yellow taxi service, year 2019
# # Replace 'base_path' with your actual base path
# # base_path = "C:/Users/sai/Downloads/yellow_tripdata_2019-"

# # # Process and upload files for the months from January to December
# # for i in range(3, 13):  # Starting from February (02) to December (12)
# #     local_file_path = f"{base_path}{i:02d}.csv.gz"
# #     gcs_object_path = f"yellow/2019/yellow_tripdata_2019-{i:02d}.parquet"
# #     process_and_upload(local_file_path, gcs_object_path)

# base_path = "C:/Users/sai/Downloads/yellow_tripdata_2020-"

# # Process and upload files for the months from January to December
# for i in range(2, 3):  # Starting from February (02) to December (12)
#     local_file_path = f"{base_path}{i:02d}.csv.gz"
#     gcs_object_path = f"yellow/2020/yellow_tripdata_2020-{i:02d}.parquet"
#     process_and_upload(local_file_path, gcs_object_path)


#### NEW TRY


import os
import pandas as pd
from google.cloud import storage

# Path to your GCP service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\sai\Downloads\DE_Project_git_connected\DE_OLD\week1_set_up\Gcp_Terraform\keys.json"

# Specify your GCS bucket name
os.environ["GCP_GCS_BUCKET"] = "mage_testing"

def upload_to_gcs(bucket, object_name, local_file):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)

def process_and_upload(local_file_path, gcs_object_path):
    try:
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
        parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']

        # Read the CSV file into a Pandas DataFrame with specified data types and parse_dates
        df = pd.read_csv(local_file_path, dtype=taxi_dtypes, parse_dates=parse_dates)

        # Convert DataFrame to Parquet format using pyarrow
        parquet_file_path = local_file_path.replace('.csv.gz', '.parquet')
        df.to_parquet(parquet_file_path, engine='pyarrow')

        # Upload the Parquet file to GCS
        upload_to_gcs(os.environ["GCP_GCS_BUCKET"], gcs_object_path, parquet_file_path)

        print(f"Parquet file '{parquet_file_path}' uploaded to GCS as '{gcs_object_path}'")

    except Exception as e:
        print(f"Error processing {local_file_path}: {e}")

# Example usage for yellow taxi service, year 2020
base_path = "C:/Users/sai/Downloads/yellow_tripdata_2020-"

# Process and upload files for the months from February (02) to December (12)
for i in range(1, 13):  # Starting from February (02) to December (12)
    local_file_path = f"{base_path}{i:02d}.csv.gz"
    gcs_object_path = f"yellow_1/2020/yellow_tripdata_2020-{i:02d}.parquet"
    process_and_upload(local_file_path, gcs_object_path)
