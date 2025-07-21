-- Last updated: 7/21/2025, 12:59:47 AM
# Write your MySQL query statement below

select p.project_id, round(avg(e.experience_years),2) as average_years
from project p
join employee e on e.employee_id = p.employee_id
group by p.project_id;
