-- creates the table unique_id
-- description:
--      id int with the default value 1 and will be unique
--      name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- ignore if the table unique_id already exists
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
