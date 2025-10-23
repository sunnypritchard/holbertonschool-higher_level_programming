-- Retrieve the titles of all TV shows that belong to the 'Comedy' genre
-- The results are ordered by the TV show title in ascending order
SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
