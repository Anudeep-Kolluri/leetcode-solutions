-- Last updated: 7/21/2025, 12:59:42 AM
-- Write your PostgreSQL query statement below
with cte as (
    select
    customer_pref_delivery_date::date - order_date::date as temp,
    row_number() over(partition by customer_id order by order_date::date asc)
    from delivery
)

select 
round((1.0 - avg(
    case
        when temp != 0 then 1
        else 0
    end
)) * 100.0, 2) as immediate_percentage
from cte
where row_number = 1;