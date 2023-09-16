#!/usr/bin/python3
"""
    this module has a script that lists all states from a database,
    where name matches the argument. But safe from MySQL injections
    using MySQLdb module.

    Functions:
    establising_connection(): works as the name says connect to the MySQL db.
    result(): execute the SQL query and fetch the result.
"""
import MySQLdb
import sys
import re


def escape(string):
    """
    this function will check the if the given argument safe from MySQL
    injections.
    Returns:
        a string safe from MySQL injections.
    """
    characters = r'[\'\"\\]'
    escape_char = r'\\\\\\1'
    return re.sub(characters, escape_char, string)


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
    ARG = escape(sys.argv[4])
    query = 'SELECT id, name FROM states WHERE'\
            '`name` = "{}" ORDER BY id ASC'.format(ARG)
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


if __name__ == '__main__':
    for row in result():
        print(row)
