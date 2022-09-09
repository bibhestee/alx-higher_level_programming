-- creates the database hbtn_0d_usa
-- creates the table cities
-- cities description:
--      id int unique, auto generated, can't be null and is a primary key
--      state_id int, can't be null and must be a foreign key that references to ido of the states table
--      name VARCHAR(256) can't be null
-- ignore if the database hbtn_0d_usa already exists
-- ignore table creation if the table cities already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(state_id)
        REFERENCES states (id)
);
