-- Last updated: 7/21/2025, 1:00:57 AM
-- Write your PostgreSQL query statement below
SELECT 
  (SELECT DISTINCT salary
   FROM Employee
   ORDER BY salary DESC
   LIMIT 1 OFFSET 1) as SecondHighestSalary