-- Script that creates the table id_not_null on MySQL server
-- id INT with default value 1
-- name VARCHAR(256)
-- If the table already exists, script should not fail
-- Database name will be passed as argument to mysql command
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
