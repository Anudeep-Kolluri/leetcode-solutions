-- Last updated: 7/21/2025, 12:59:33 AM
# Write your MySQL query statement below
SELECT eu.unique_id, e.name FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;