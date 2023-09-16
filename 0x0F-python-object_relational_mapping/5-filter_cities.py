#!/usr/bin/python3
"""
    this module has a script that takes in the name of a state and
    lists all cities from a database, using MySQLdb module.

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
        'SELECT c.name FROM cities c, states s WHERE s.name = "{}" AND state_id = s.id ORDER BY c.id ASC'.format(sys.argv[4]))
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


if __name__ == '__main__':
    i = 0
    for row in result():
        length = len(result())
        for col in row:
            print(col, end='')
            i += 1
            if (length != i):
                print('', end=', ')
    print()
