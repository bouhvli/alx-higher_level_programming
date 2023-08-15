-- creates a table second_table in the database hbtn_0c_0
-- and add multiples rows.
CREATE TABLE IF NOT EXISTS  second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
-- new line in
INSERT INTO second_table VALUES (1, 'John', 10);
-- new line in
INSERT INTO second_table VALUES (2, 'Alex', 3);
-- new line in
INSERT INTO second_table VALUES (3, 'Bob', 14);
-- new line in
INSERT INTO second_table VALUES (4, 'George', 8);
