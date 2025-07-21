-- Last updated: 7/21/2025, 12:59:42 AM
-- Write your PostgreSQL query statement below
with unik as (
    select distinct product_id from
    products
),
cte as (
    select product_id, change_date, new_price, 
    row_number() over(partition by product_id order by change_date::date desc)
    from products
    where change_date <= '2019-08-16'
), dbs as (
    select unik.product_id, COALESCE(cte.new_price, 10) as price, COALESCE(row_number, 1) as rn
    from unik
    left join cte
    on unik.product_id = cte.product_id
    )
    
select dbs.product_id,  dbs.price
from dbs
where dbs.rn = 1;