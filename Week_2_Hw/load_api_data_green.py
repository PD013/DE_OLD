import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    


    base_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/"
    
    # Generate the URL for the specific month
    urls = [f"{base_url}green_tripdata_2020-{month:02d}.csv.gz" for month in range(10, 13)]


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
        'ehail_fee' : float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float 
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    all_data = pd.concat([pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates) for url in urls], ignore_index=True)

    return all_data


final_three_months_data = load_data_from_api()
