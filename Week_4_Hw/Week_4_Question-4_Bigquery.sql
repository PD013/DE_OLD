# This is where I have solved Question 4 
-- Question 4 (2 points)
-- What is the service that had the most rides during the month of July 2019 month with the biggest amount of rides after building a tile for the fact_fhv_trips table and the fact_trips tile as seen in the videos?


### UNIONALL ALL THE PART 

SELECT 
    service_type,
    COUNT(*) AS trip_count
FROM 
    `dtc-de-course-412810.dbt_pdesai.fact_fhv_trips` 
WHERE 
    pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
GROUP BY 
    service_type

UNION ALL 

SELECT 
    service_type,
    COUNT(*) AS trip_count
FROM 
    `dtc-de-course-412810.dbt_pdesai.fact_trips` 
WHERE 
    pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
GROUP BY 
    service_type

UNION ALL

SELECT 
    'Green + FHV' AS service_type,
    SUM(trip_count) AS trip_count
FROM (
SELECT 
    service_type,
    COUNT(*) AS trip_count
FROM 
    `dtc-de-course-412810.dbt_pdesai.fact_fhv_trips` 
WHERE 
    pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
GROUP BY 
    service_type

UNION ALL 

SELECT 
    service_type,
    COUNT(*) AS trip_count
FROM 
    `dtc-de-course-412810.dbt_pdesai.fact_trips` 
WHERE 
    pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
GROUP BY 
    service_type
) as temp1
where service_type = 'fhv' 
OR service_type = 'Green';


### THIS IS MORE OPTIMIZED QUERY USing CTEs

WITH fhv_counts AS (
    SELECT 
        'FHV' AS service_type,
        COUNT(*) AS trip_count
    FROM 
        `dtc-de-course-412810.dbt_pdesai.fact_fhv_trips` 
    WHERE 
        pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
    GROUP BY 
        service_type
),

other_counts AS (
    SELECT 
        service_type,
        COUNT(*) AS trip_count
    FROM 
        `dtc-de-course-412810.dbt_pdesai.fact_trips` 
    WHERE 
        pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
    GROUP BY 
        service_type
),

combined_counts AS (
    SELECT 
        'Green + FHV' AS service_type,
        SUM(trip_count) AS trip_count
    FROM (
        SELECT 
            service_type,
            COUNT(*) AS trip_count
        FROM 
            `dtc-de-course-412810.dbt_pdesai.fact_fhv_trips` 
        WHERE 
            pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
        GROUP BY 
            service_type

        UNION ALL 

        SELECT 
            service_type,
            COUNT(*) AS trip_count
        FROM 
            `dtc-de-course-412810.dbt_pdesai.fact_trips` 
        WHERE 
            pickup_datetime BETWEEN TIMESTAMP('2019-07-01 00:00:00') AND TIMESTAMP('2019-07-31 23:59:59')
        GROUP BY 
            service_type
    ) AS temp1
    WHERE 
        service_type = 'fhv' OR service_type = 'Green'
)

SELECT * FROM fhv_counts
UNION ALL
SELECT * FROM other_counts
UNION ALL
SELECT * FROM combined_counts;



