-- Last updated: 7/21/2025, 1:00:02 AM
select  name from salesperson where sales_id not in (
    select sales_id from orders where com_id in 
        (select com_id from company where name = "RED")
)