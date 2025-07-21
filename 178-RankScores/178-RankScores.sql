-- Last updated: 7/21/2025, 1:00:55 AM
# Write your MySQL query statement below
WITH CTE AS (
SELECT t.score, ROW_NUMBER() OVER(ORDER BY t.score DESC) AS "rank" FROM (
    SELECT DISTINCT(SCORE) FROM SCORES
) as t
)
SELECT s.score, CTE.rank FROM SCORES s
LEFT JOIN CTE ON CTE.score = s.score
ORDER BY CTE.rank;