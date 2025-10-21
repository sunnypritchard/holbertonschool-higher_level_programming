-- List all scores from second_table grouped by score and show the number of occurrences for each score
-- ordered by score descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
