-- Script that creates the database hbtn_0d_usa and table states
-- id INT with default value 1, AUTO_INCREMENT and PRIMARY KEY
-- name VARCHAR(256) that cannot be NULL
-- If the database or table already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
