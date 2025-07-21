-- Last updated: 7/21/2025, 1:00:50 AM
# Write your MySQL query statement below
select email as Email
from person
group by email
having count(email) > 1;
