select
    week(timestamp) as week,
    library,
    count(distinct(system_id)) as distinct_users
from {{ ref('calls') }} as calls
group by
    week(timestamp),
    library
order by week(timestamp) desc
