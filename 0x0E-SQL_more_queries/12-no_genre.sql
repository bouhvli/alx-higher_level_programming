-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tvs.title AS 'title', COALESCE(tvsg.genre_id) AS 'genre_id'
FROM tv_shows tvs LEFT JOIN tv_show_genres tvsg ON tvs.id = tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title, tvsg.genre_id ASC;