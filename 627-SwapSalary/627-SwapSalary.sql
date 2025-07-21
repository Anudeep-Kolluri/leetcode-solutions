-- Last updated: 7/21/2025, 12:59:57 AM
# Write your MySQL query statement below

update Salary
set sex = (
    case when sex = "m" then "f" else "m" end
)