-- Last updated: 7/21/2025, 1:00:11 AM
# Write your MySQL query statement below
WITH CTE AS (
SELECT managerId as id FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5
)
SELECT e.name FROM Employee e
RIGHT JOIN CTE on e.id = CTE.id
WHERE e.id IS NOT NULL;