-- Retrieve the title of each TV show along with its associated genre IDs
-- for shows that do not have any genres assigned
-- The results are ordered by the TV show title in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

