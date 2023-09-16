#!/usr/bin/python3
"""
    this module has a script that lists all states from a database,
    with name starting with N, using MySQLdb module.

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
        "SELECT id, name FROM states WHERE name LIKE 'N%'  ORDER BY id ASC")
    res = cur.fetchall()
    return res


if __name__ == '__main__':
    for row in result():
        print(row)
