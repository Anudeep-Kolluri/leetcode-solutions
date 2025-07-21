-- Last updated: 7/21/2025, 12:59:59 AM
# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE (id % 2 = 1) AND (description != "boring")
ORDER BY rating DESC;