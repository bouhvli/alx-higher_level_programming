-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tvs.title AS 'title', tvsg.genre_id AS 'genre_id'
FROM tv_shows tvs JOIN tv_show_genres tvsg ON tvs.id = tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id ASC;
