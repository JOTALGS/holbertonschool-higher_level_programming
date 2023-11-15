-- Create table and fill some info
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table(id, name, score) VALUE (1, 'Jhon', 10)

INSERT INTO second_table(id, name, score) VALUE (2, 'Alex', 3)

INSERT INTO second_table(id, name, score) VALUE (3, 'Bob', 14)

INSERT INTO second_table(id, name, score) VALUE (4, 'George', 8)
