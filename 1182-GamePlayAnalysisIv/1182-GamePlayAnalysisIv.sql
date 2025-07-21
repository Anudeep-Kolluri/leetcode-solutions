-- Last updated: 7/21/2025, 12:59:45 AM
-- Write your PostgreSQL query statement below
with cte as (
    select
    player_id, lead(event_date) over(partition by player_id order by event_date) - event_date::date as gap,
    row_number() over(partition by player_id order by event_date)
    from activity
), cte2 as (
    select player_id, count(distinct(gap)) filter(where gap = 1 and row_number = 1)
    from cte
    group by player_id
)

select round(sum(cte2.count)/count(*)::numeric, 2) as fraction from cte2;