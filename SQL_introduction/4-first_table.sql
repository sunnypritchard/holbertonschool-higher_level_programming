-- Create a table named 'first_table' in the current database named 'hbtn_0c_0'
-- The table should have two columns: 'id' (int) and 'name' (varchar(256))
-- If the table already exists, do not raise an error.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
