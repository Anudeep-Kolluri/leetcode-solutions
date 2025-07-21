-- Last updated: 7/21/2025, 12:59:49 AM
# Write your MySQL query statement below

select actor_id, director_id from ActorDirector
group by actor_id, director_id
having count(actor_id) > 2;