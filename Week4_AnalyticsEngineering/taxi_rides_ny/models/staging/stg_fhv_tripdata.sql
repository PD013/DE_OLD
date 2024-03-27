{{
    config(
        materialized='view'
    )
}}

select
    dispatching_base_num,

    cast(pickup_datetime as timestamp) AS pickup_datetime,
    cast(dropoff_datetime as timestamp) AS dropoff_datetime,
        
    cast(pulocationid as integer) AS pickup_locationid,
    cast(dolocationid as integer) AS dropoff_locationid,
    
    sr_flag,

from {{ source('staging', 'fhv_tripdata') }}
    
    