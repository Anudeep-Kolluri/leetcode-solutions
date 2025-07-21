-- Last updated: 7/21/2025, 1:00:54 AM
# Write your MySQL query statement below
WITH CTE AS (
SELECT id, (DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC)) as idx FROM Employee
)
SELECT 
d.name as Department,
e.name as Employee,
e.salary as Salary
FROM Employee e
RIGHT JOIN CTE ON CTE.id = e.id
LEFT JOIN Department d ON d.id = e.departmentId
WHERE CTE.idx <= 3;


