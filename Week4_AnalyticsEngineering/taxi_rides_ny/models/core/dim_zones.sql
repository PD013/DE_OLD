{{ config(
    materialized='table',
    location='US'
) }}

select 
    locationid, 
    borough, 
    zone, 
    -- Here just in the green data everthing that was boro was green so just changing it/replacing it
    replace(service_zone,'Boro','Green') as service_zone 
from {{ ref('taxi_zone_lookup') }}
