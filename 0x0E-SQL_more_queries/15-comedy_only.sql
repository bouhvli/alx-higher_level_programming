-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title AS 'title'
FROM tv_shows JOIN tv_show_genres JOIN tv_genres
ON tv_genres.name = 'Comedy'
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
