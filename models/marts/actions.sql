{{
    config(
        re_data_monitored=true,
        re_data_time_filter='date',
    )
}}


select
    system_id,
    library,
    re_data_version,
    to_date(timestamp) as date,
    array_agg(distinct command) as commands,
    min(timestamp) as min_timestamp,
    max(timestamp) as max_timestamp,
    count(*) as count
from {{ ref('calls')}}
group by
    system_id, library, re_data_version, to_date(timestamp)
order by to_date(timestamp) desc
