-- Last updated: 7/21/2025, 12:58:06 AM
# Write your MySQL query statement below

with cte as (
    select
    user_id, count(action) as ct
    from confirmations
    where action = 'confirmed'
    group by user_id
)
select
s.user_id, 
case
when cte.ct/count(s.user_id) is null then 0 else round(cte.ct/count(s.user_id), 2)
end as confirmation_rate
from signups s
left join confirmations c
on c.user_id = s.user_id
left join cte
on cte.user_id = c.user_id
group by s.user_id;