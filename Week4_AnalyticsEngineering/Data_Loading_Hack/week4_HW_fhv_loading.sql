# Here we downloaded the csv.gz files and uploaded in the gcs/I did manually it can be automated 
# Just download csv.gz and upload as it is and then run the below the problem of data types are gone completely

CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-412810.trips_data_all.fhv_tripdata` 
OPTIONS (
  format = 'CSV',
  uris = ['gs://mage_testing/fhv/end/fhv_tripdata_2019-*.csv.gz']
);

