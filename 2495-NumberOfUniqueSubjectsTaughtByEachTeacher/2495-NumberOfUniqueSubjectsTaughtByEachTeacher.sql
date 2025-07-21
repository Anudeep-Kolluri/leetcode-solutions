-- Last updated: 7/21/2025, 12:59:13 AM
# Write your MySQL query statement below

select
t.teacher_id, count(distinct t.subject_id) as cnt
from teacher t
group by t.teacher_id;