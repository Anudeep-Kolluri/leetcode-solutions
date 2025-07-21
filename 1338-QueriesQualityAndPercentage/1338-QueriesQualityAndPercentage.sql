-- Last updated: 7/21/2025, 12:59:39 AM
-- Write your PostgreSQL query statement below
with cte as (
    select
    q.query_name, round(avg(q.rating::float/q.position)::numeric, 2) as quality, 
    round(count(
        case
            when q.rating < 3 then 1
        end
    )::numeric/count(q.rating)*100, 2) as poor_query_percentage
    from queries q
    group by q.query_name
)

select cte.query_name, cte.quality, cte.poor_query_percentage
from cte;