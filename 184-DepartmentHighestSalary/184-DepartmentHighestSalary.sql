-- Last updated: 7/21/2025, 1:00:49 AM
-- Write your PostgreSQL query statement below
with cte as (
    select d.name as department, e.name as employee, e.salary as salary, 
    rank() over(partition by d.name order by e.salary desc)
    from employee e
    left join department d
    on e.departmentId = d.id
)
select department, employee, salary
from cte
where rank = 1
;