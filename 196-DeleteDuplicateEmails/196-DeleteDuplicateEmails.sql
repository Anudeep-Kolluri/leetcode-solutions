-- Last updated: 7/21/2025, 1:00:52 AM
delete from person
where id not in
(select min(id) from person
group by email);