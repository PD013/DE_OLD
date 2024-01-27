SELECT
  lpep_pickup_datetime::date AS pickup_day,
  MAX(trip_distance) AS max_trip_distance
FROM
  green_taxi_data_sept
GROUP BY
  pickup_day
ORDER BY max_trip_distance DESC;

-- Answer :- 2019-09-26
