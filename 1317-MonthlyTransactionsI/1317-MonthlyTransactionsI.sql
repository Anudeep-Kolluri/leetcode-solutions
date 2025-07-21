-- Last updated: 7/21/2025, 12:59:41 AM
WITH CTE AS (
    SELECT * FROM Transactions
    WHERE state = "approved"
)
SELECT 
DATE_FORMAT(t.trans_date, "%Y-%m") as month,
t.country,
COUNT(t.id) as trans_count,
COALESCE(COUNT(CTE.id),0) as approved_count,
SUM(t.amount) as trans_total_amount,
COALESCE(SUM(CTE.amount),0) as approved_total_amount
FROM Transactions t
LEFT JOIN CTE ON CTE.id = t.id
GROUP BY month, t.country;
