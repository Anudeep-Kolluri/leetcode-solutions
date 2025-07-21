-- Last updated: 7/21/2025, 1:00:07 AM
-- Write your PostgreSQL query statement below

select round(sum(tiv_2016)::numeric, 2) as tiv_2016
from insurance i1
where 
    exists (
        select * from insurance i2
        where i2.tiv_2015 = i1.tiv_2015 and
        i2.pid != i1.pid
    )
and
    not exists (
        select * from insurance i2
        where i2.lat = i1.lat
        and i2.lon = i1.lon
        and i2.pid != i1.pid
    )