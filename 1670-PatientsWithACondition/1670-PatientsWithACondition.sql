-- Last updated: 7/21/2025, 12:59:29 AM
select
*
from patients
where (conditions like 'DIAB1%') or (conditions like '% DIAB1%');