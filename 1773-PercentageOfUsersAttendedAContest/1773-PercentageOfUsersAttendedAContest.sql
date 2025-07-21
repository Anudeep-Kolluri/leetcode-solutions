-- Last updated: 7/21/2025, 12:59:27 AM
WITH cte AS (
    SELECT
        r.contest_id, 
        COUNT(DISTINCT r.user_id) AS c
    FROM register r
    GROUP BY r.contest_id
), 
u AS (
    SELECT COUNT(DISTINCT user_id) AS c
    FROM users
)

SELECT 
    cte.contest_id, 
    round(((cte.c::float / u.c) * 100)::numeric, 2) as percentage
FROM cte, u
order by percentage desc, cte.contest_id asc
;
