-- lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres JOIN tv_show_genres JOIN tv_shows
ON tv_shows.title = 'Dexter'
WHERE tv_shows.id = tv_show_genres.show_id
AND tv_genres.id = tv_show_genres.genre_id;
