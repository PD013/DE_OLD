# Week 4 Homework

## Question 1:
**What happens when we execute `dbt build --vars '{"is_test_run":"true"}'`?**

Answer: It applies a limit of 100 only to our staging models.

## Question 2:
**What is the code that our CI job will run? Where is this code coming from?**

Answer: The code from the development branch we are requesting to merge to the main.

## Question 3 (2 points):
**What is the count of records in the model `fact_fhv_trips` after running all dependencies with the test run variable disabled (`"is_test_run":"false"`)?**

Answer: 22,998,722

## Question 4 (2 points):
**What is the service that had the most rides during the month of July 2019 with the biggest amount of rides after building a tile for the `fact_fhv_trips` table and the `fact_trips` tile as seen in the videos?**

* [Week_4_Question-4](Week_4_Hw/Week_4_Question-4.sql) 

Create a dashboard with some tiles that you find interesting to explore the data. One tile should show the amount of trips per month, as done in the videos for `fact_trips`, including the `fact_fhv_trips` data.
