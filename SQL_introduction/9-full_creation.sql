-- Create a table named 'second_table' in the current database named 'hbtn_0c_0'
-- The table should have three columns: 'id' (int), 'name' (varchar(256)), and 'score' (int)
-- If the table already exists, do not raise an error.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
