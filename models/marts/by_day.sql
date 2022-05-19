select
    to_date(timestamp) as date,
    count(distinct(user_id)) as distinct_users
from {{ ref('calls') }} as calls
where
    timestamp > '2022-03-24' :: timestamp and (status = 'success' or command = 'serve')
group by to_date(timestamp)
order by to_date(timestamp) desc
