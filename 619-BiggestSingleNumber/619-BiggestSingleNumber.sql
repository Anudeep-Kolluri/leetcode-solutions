-- Last updated: 7/21/2025, 12:59:59 AM
SELECT max(num) as num
from (
    select num from MyNumbers
    group by num
    having count(num) = 1
) as unique_table;