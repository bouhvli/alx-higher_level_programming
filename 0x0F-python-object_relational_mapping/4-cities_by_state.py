#!/usr/bin/python3
"""
    this module has a script that lists all cities from a database,
    using MySQLdb module.

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
    cur.execute(
        'SELECT cities.id, cities.name, states.name FROM cities,'
        'states WHERE state_id = states.id ORDER BY cities.id ASC')
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


if __name__ == '__main__':
    for row in result():
        print(row)
