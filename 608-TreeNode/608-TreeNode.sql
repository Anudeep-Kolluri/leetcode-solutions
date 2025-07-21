-- Last updated: 7/21/2025, 1:00:01 AM
-- Write your PostgreSQL query statement below
select id,
case
    when p_id is null then 'Root'
    when id in (select p_id from tree) then 'Inner'
    else 'Leaf'
end as type
from tree;
