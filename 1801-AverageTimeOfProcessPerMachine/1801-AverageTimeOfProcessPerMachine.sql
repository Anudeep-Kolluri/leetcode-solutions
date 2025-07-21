-- Last updated: 7/21/2025, 12:59:25 AM
# Write your MySQL query statement below
select a.machine_id, 
ROUND(
    AVG(CASE WHEN a.activity_type='end' THEN a.timestamp END) -
    AVG(CASE WHEN a.activity_type='start' THEN a.timestamp END), 3
) as processing_time
FROM activity a
group by a.machine_id;