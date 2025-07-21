-- Last updated: 7/21/2025, 12:59:38 AM
-- select

-- from students st
-- cross join subjects su;


with cte as (
    select
    st.student_id as student_id,
    st.student_name as student_name,
    su.subject_name as subject_name
    from students st
    cross join subjects su
)
select
cte.student_id as student_id,
cte.student_name as student_name,
cte.subject_name as subject_name,
count(ex.student_id) as attended_exams
from cte
left join examinations ex
on ex.student_id = cte.student_id
and ex.subject_name = cte.subject_name
group by cte.student_name, cte.subject_name
order by cte.student_id, cte.subject_name;