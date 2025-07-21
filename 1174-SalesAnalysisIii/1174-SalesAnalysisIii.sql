-- Last updated: 7/21/2025, 12:59:46 AM
-- Write your PostgreSQL query statement below

select s.product_id, any_value(p.product_name) as product_name
from sales s
left join product p
on s.product_id = p.product_id
where p.product_id not in (select t.product_id from sales t where 
    not (sale_date between '2019-01-01' and '2019-03-31'))
group by s.product_id;


-- select t.product_id from sales t where 
--     not (sale_date between '2019-01-01' and '2019-03-31');