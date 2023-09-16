#!/usr/bin/python3
"""
    this module has a script that lists all states from a database,
    where name matches the argument. using MySQLdb module.

    Functions:
    establising_connection(): works as the name says connect to the MySQL db.
    result(): execute the SQL query and fetch the result.
"""
import MySQLdb
import sys


def establising_connection():
    """
    this function establich the connection to MySQL DB.

    Returns:
        the object of Mysqldb connection.
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    return db


def result():
    """
    this function will execute the SQL query and fetch the result.

    Returns:
        the list of tuples.
    """
    db = establising_connection()
    cur = db.cursor()
    query = 'SELECT id, name FROM states WHERE'\
            '`name` LIKE BINARY "{}" ORDER BY id ASC'.format(sys.argv[4])
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


if __name__ == '__main__':
    for row in result():
        print(row)
