-- This SQL query selects the score and name columns from the second_table
-- It filters out any rows where the name is NULL
-- Finally, it orders the results by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
