-- Last updated: 7/21/2025, 12:59:40 AM
-- Write your PostgreSQL query statement below
with cte as (
    select *, sum(weight) over(order by turn)
    from queue
    order by turn
)

select person_name
from cte
where sum <= 1000
order by sum desc
limit 1;