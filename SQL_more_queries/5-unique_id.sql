-- Script that creates the table unique_id on MySQL server
-- id INT with default value 1 and UNIQUE constraint
-- name VARCHAR(256)
-- If the table already exists, script should not fail
-- Database name will be passed as argument to mysql command
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
