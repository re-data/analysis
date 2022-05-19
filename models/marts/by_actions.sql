select
    user_id,
    os_system,
    dbt_version,
    re_data_version,
    python_version,
    to_date(timestamp) as date,
    array_agg(distinct command) as commands,
    min(timestamp) as min_timestamp,
    max(timestamp) as max_timestamp,
    count(*)
from {{ ref('calls')}}
where
    timestamp > '2022-05-06' :: timestamp and
    (status = 'success' or command = 'serve')
group by
    user_id, os_system, dbt_version, re_data_version, python_version, to_date(timestamp)
order by to_date(timestamp) desc;
