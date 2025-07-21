-- Last updated: 7/21/2025, 12:59:50 AM
# Write your MySQL query statement below

select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select count(*) from product);