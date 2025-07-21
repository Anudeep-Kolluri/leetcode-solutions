-- Last updated: 7/21/2025, 12:59:48 AM
# Write your MySQL query statement below
select product_name, year, price from Sales s
join Product p on s.product_id = p.product_id;