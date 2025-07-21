-- Last updated: 7/21/2025, 1:00:06 AM
# Write your MySQL query statement below
select customer_number from Orders
group by customer_number
order by count(customer_number) desc
limit 1;