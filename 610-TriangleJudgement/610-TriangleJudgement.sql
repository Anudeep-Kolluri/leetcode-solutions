-- Last updated: 7/21/2025, 1:00:00 AM
# Write your MySQL query statement below

select *, if(x+y>z and y+z>x and x+z>y, "Yes", "No") as triangle from Triangle;