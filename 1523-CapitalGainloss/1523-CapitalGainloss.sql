-- Last updated: 7/21/2025, 12:59:32 AM
-- Write your PostgreSQL query statement below
with cte as (
    select stock_name, operation, sum(price) as price
    from stocks
    group by stock_name, operation
)

select stock_name,
sum (case
    when operation = 'Sell' then price
    else -price
end) as capital_gain_loss
from cte
group by stock_name;