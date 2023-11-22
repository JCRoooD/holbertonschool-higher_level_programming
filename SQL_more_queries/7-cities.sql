-- creating table cities
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL UNIQUE, state_id INT NOT NULL, name VARCHAR(256) NOT NULL);