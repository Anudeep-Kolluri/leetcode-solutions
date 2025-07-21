-- Last updated: 7/21/2025, 12:59:28 AM
# Write your MySQL query statement below
with cte as(
select v.customer_id as customer_id from transactions t
right join visits v on v.visit_id = t.visit_id
where t.transaction_id is NULL
)
select customer_id, count(customer_id)  as count_no_trans from cte
group by customer_id;