-- Retrieve the title of each TV show along with its associated genre IDs
-- The results are ordered by the TV show title and genre ID in ascending order
-- Use LEFT JOIN to include shows without genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
