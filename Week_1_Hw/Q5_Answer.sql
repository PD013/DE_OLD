SELECT
  T."Borough",
  SUM(G.total_amount) AS total_amount_sum
FROM
  green_taxi_data_sept AS G
INNER JOIN
  taxi_zone_data AS T
ON
  G."PULocationID" = T."LocationID"
WHERE
  G.lpep_pickup_datetime::date = '2019-09-18'
  AND T."Borough" != 'Unknown'
GROUP BY
  T."Borough"
HAVING
  SUM(G.total_amount) > 50000
ORDER BY
  total_amount_sum DESC
LIMIT 3;

Answer :- "Brooklyn" "Manhattan" "Queens"
