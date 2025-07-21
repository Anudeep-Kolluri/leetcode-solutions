-- Last updated: 7/21/2025, 12:59:38 AM
# Write your MySQL query statement below
with cte as(
    select
    u.product_id, round(sum(u.units * p.price)/sum(u.units),2) as average_price
    from prices p
    left join unitssold u
    on u.product_id = p.product_id
    where u.purchase_date between p.start_date and p.end_date
    group by u.product_id
)
select distinct p.product_id,
case
when cte.average_price is not null then cte.average_price else 0
end as average_price
from prices p
left join cte on p.product_id = cte.product_id;


