# Here We Create Table from the marketplace data 

# Creating green_tripdata Table
CREATE TABLE `dtc-de-course-412810.trips_data_all.green_tripdata` as 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2019` ;


# Creating yellow_tripdata Table
CREATE TABLE `dtc-de-course-412810.trips_data_all.yellow_tripdata` as 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2019` ;



# Inserting in green and yellow the 2020 data also
INSERT INTO `dtc-de-course-412810.trips_data_all.green_tripdata` 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2020` ;


INSERT INTO  `dtc-de-course-412810.trips_data_all.yellow_tripdata`  
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2020` ;


