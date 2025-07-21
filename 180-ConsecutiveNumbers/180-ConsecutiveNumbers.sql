-- Last updated: 7/21/2025, 1:00:53 AM
# Write your MySQL query statement below

SELECT DISTINCT(consec.con) as ConsecutiveNums FROM (
SELECT
CASE
WHEN (LEAD(num) OVER(ORDER BY id) = num) AND (LAG(num) OVER(ORDER BY id) = num) THEN num
END as con
FROM Logs)
AS consec
WHERE consec.con IS NOT NULL;