-- List all cities with their state names from database hbtn_0d_usa
-- Display: cities.id - cities.name - states.name
-- Results sorted by cities.id in ascending order
-- Database name passed as argument to mysql command
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
