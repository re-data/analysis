select
    system_id,
    library,
    to_date(timestamp) as date,
    array_agg(distinct command) as commands,
    min(timestamp) as min_timestamp,
    max(timestamp) as max_timestamp,
    count(*) as count
from {{ ref('calls')}}
group by
    system_id, library, to_date(timestamp)
order by to_date(timestamp) desc
