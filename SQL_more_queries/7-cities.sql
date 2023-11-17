-- create database and add a table to it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id          INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
    state_id    INT NOT NULL,
    name        VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
    );
