-- Last updated: 7/21/2025, 12:59:44 AM
# Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from Activity
where activity_date > "2019-06-27" and activity_date < "2019-07-28"
group by activity_date;