-- Last updated: 7/21/2025, 12:59:36 AM
WITH CTE AS (SELECT visited_on, SUM(amount) AS days_sum FROM customer
GROUP BY visited_on
ORDER BY visited_on ASC)

SELECT visited_on,
SUM(days_sum) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
ROUND(AVG(days_sum) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM CTE 
OFFSET 6