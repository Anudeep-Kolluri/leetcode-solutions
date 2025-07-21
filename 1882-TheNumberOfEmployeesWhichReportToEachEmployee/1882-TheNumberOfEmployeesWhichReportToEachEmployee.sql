-- Last updated: 7/21/2025, 12:59:22 AM
-- Write your PostgreSQL query statement below

with cte as
(
    select reports_to, round(avg(age),0) as average_age, count(age) as reports_count
    from employees
    where reports_to is not null
    group by reports_to
)

select e.employee_id, e.name, r.reports_count, r.average_age
from cte r
left join employees e on e.employee_id = r.reports_to
order by employee_id;