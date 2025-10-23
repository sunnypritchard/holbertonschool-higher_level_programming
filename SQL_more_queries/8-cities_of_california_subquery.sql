-- List all cities of California from the database hbtn_0d_usa
-- Results sorted by cities.id in ascending order
-- Using subquery (no JOIN allowed)
-- Database name passed as argument to mysql command
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
