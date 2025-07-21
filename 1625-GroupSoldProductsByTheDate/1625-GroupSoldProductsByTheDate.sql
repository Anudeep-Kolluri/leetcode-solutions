-- Last updated: 7/21/2025, 12:59:30 AM
-- Write your PostgreSQL query statement below

select 
    sell_date,
    count(distinct product) as num_sold,
    string_agg(distinct product, ',') as products
from
    activities


group by sell_date
order by sell_date;