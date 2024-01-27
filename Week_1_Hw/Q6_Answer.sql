# STEP 1 - We will find the DropOff Location Id using which find the Zone 
SELECT G."DOLocationID" , MAX(G."tip_amount") as tip
FROM
  green_taxi_data_sept AS G
INNER JOIN
  taxi_zone_data AS T
ON
  G."PULocationID" = T."LocationID"
WHERE G.lpep_pickup_datetime::date BETWEEN '2019-09-01' and '2019-09-30'
AND T."Zone" = 'Astoria'
GROUP BY G."DOLocationID"
ORDER BY tip DESC
LIMIT 1;

# Step 2 Using the DOLocationID find the Zone
SELECT T."Zone"
FROM taxi_zone_data as T
WHERE t."LocationID" = '132';

## Answer - JFK airport
