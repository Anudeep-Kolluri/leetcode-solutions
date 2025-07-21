-- Last updated: 7/21/2025, 12:59:43 AM
# Write your MySQL query statement below
SELECT DISTINCT(author_id) as id FROM Views
WHERE author_id = viewer_id
ORDER BY id;