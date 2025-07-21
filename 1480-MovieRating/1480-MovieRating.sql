-- Last updated: 7/21/2025, 12:59:34 AM
-- Write your PostgreSQL query statement below
with cte as (
    select mm.title, u.name, m.rating, m.created_at
    from movierating m
    left join users u on m.user_id = u.user_id
    left join movies mm on m.movie_id = mm.movie_id
)
select results from
(
    (
        select title as results, avg(rating) as top_results
        from cte
        where created_at between '2020-02-01' and '2020-02-29'
        group by results
        order by top_results desc, results asc
        limit 1
    )
    union all
    (
        select name as results, count(name) as top_results
        from cte
        group by results
        order by top_results desc, results asc
        limit 1
    )
);