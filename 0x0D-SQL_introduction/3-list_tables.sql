-- a script that lists all the tables of a database in your MySQL server.
SELECT table_name
FROM information_schema.tables
where table_schema = DATABASE()
AND table_type = 'BASE TABLE';
