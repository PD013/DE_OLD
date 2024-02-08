# Pipeline : green_taxi_etl

![image](https://github.com/PD013/Data_Engineering-Zoomcamp/assets/114251906/b50f239e-1798-433a-93cc-475f24a8b6cf)

## [Load_api_data_green](https://github.com/PD013/Data_Engineering-Zoomcamp/blob/main/Week_2_Hw/load_api_data_green.py)
## [transform_green_taxi_data](https://github.com/PD013/Data_Engineering-Zoomcamp/blob/main/Week_2_Hw/transform_green_taxi_data.py)
## [green_taxi_to_gcs_partitioned_parquet.](https://github.com/PD013/Data_Engineering-Zoomcamp/blob/main/Week_2_Hw/green_taxi_to_gcs_partitioned_parquet.py)
## [green_taxi_data_to_postgress](https://github.com/PD013/Data_Engineering-Zoomcamp/blob/main/Week_2_Hw/green_taxi_data_to_postgress.py)


### Questions

## Question 1. Data Loading

Once the dataset is loaded, what's the shape of the data?

* 266,855 rows x 20 columns
* 544,898 rows x 18 columns
* 544,898 rows x 20 columns
* 133,744 rows x 20 columns

  `` Answer :- 266,855 rows x 20 columns ``

## Question 2. Data Transformation

Upon filtering the dataset where the passenger count is greater than 0 _and_ the trip distance is greater than zero, how many rows are left?

* 544,897 rows
* 266,855 rows
* 139,370 rows
* 266,856 rows

 ``Answer :- 139,370 rows ``

## Question 3. Data Transformation

Which of the following creates a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date?

* `data = data['lpep_pickup_datetime'].date`
* `data('lpep_pickup_date') = data['lpep_pickup_datetime'].date`
* `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date`
* `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date()`

``Answer :- data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date``


## Question 4. Data Transformation

What are the existing values of `VendorID` in the dataset?

* 1, 2, or 3
* 1 or 2
* 1, 2, 3, 4
* 1

``Answer :- 1 or 2``
[Answer](testing_sql_for_green.sql)

## Question 5. Data Transformation

How many columns need to be renamed to snake case?

* 3
* 6
* 2
* 4

``Answer :- 4``


## Question 6. Data Exporting
Once exported, how many partitions (folders) are present in Google Cloud?

* 96
* 56
* 67
* 108

``Amswer :-  closest Answer is _96_ -- Foldersin GC is 95 ``
