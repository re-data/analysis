select
    to_date(timestamp) as date,
    library,
    count(distinct(system_id)) as distinct_users
from {{ ref('calls') }} as calls
group by
    to_date(timestamp),
    library
order by to_date(timestamp) desc
