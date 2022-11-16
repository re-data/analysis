{{
    config(
        re_data_monitored=true,
        re_data_time_filter='date',
    )
}}

select
    to_date(timestamp) as date,
    library,
    count(distinct(system_id)) as distinct_users
from {{ ref('exceptions') }} as calls
group by
    to_date(timestamp),
    library
order by to_date(timestamp) desc
