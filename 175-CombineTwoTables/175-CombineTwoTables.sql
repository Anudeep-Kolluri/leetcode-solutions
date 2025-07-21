-- Last updated: 7/21/2025, 1:00:59 AM
# Write your MySQL query statement below
select a.firstName, a.lastName, b.city, b.state from Address b
right join Person a on a.personId = b.personId;