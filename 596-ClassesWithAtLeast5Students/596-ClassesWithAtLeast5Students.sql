-- Last updated: 7/21/2025, 1:00:05 AM
# Write your MySQL query statement below
select class from Courses
group by class
having count(class) >= 5;