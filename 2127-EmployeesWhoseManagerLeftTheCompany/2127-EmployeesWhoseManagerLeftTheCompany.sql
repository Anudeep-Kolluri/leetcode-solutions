-- Last updated: 7/21/2025, 12:58:04 AM
-- Write your PostgreSQL query statement below

with cte as (
    select e1.employee_id, e1.salary, e2.employee_id as ext, e1.manager_id as mxt
    from employees e1
    left join employees e2
    on e1.manager_id = e2.employee_id
)

select employee_id from cte
where salary < 30000 and ext is null and mxt is not null
order by employee_id;