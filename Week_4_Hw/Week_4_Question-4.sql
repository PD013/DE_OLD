with
    fhv_counts as (
        select 'FHV' as service_type, count(*) as trip_count
        from {{ ref("fact_fhv_trips") }}
        where
            pickup_datetime between timestamp('2019-07-01 00:00:00') and timestamp(
                '2019-07-31 23:59:59'
            )
        group by service_type
    ),

    other_counts as (
        select service_type, count(*) as trip_count
        from {{ ref("fact_trips") }}
        where
            pickup_datetime between timestamp('2019-07-01 00:00:00') and timestamp(
                '2019-07-31 23:59:59'
            )
        group by service_type
    ),

    combined_counts as (
        select 'Green + FHV' as service_type, sum(trip_count) as trip_count
        from
            (
                select service_type, count(*) as trip_count
                from {{ ref("fact_fhv_trips") }}
                where
                    pickup_datetime
                    between timestamp('2019-07-01 00:00:00') and timestamp(
                        '2019-07-31 23:59:59'
                    )
                group by service_type

                union all

                select service_type, count(*) as trip_count
                from {{ ref("fact_trips") }}
                where
                    pickup_datetime
                    between timestamp('2019-07-01 00:00:00') and timestamp(
                        '2019-07-31 23:59:59'
                    )
                group by service_type
            ) as temp1
        where service_type = 'fhv' or service_type = 'Green'
    )

select *
from fhv_counts
union all
select *
from other_counts
union all
select *
from
    combined_counts
    -- HERE ALWAYS MAKE SURE NEVER USE ; IN DBT SQL
    
