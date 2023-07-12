#!/usr/bin/python3
"""
Task 12: Pascal's Triangle Technical interview preparation
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    my_list = []
    triangle = []
    if (n <= 0):
        return my_list
    else:
        for line in range(0, n):
            for row in range(0, line + 1):
                my_list.insert(row, sum(line, row))
            triangle.append(my_list)
            my_list = []
        return triangle


def fact(number):
    """
    callc the factorial of a number
    """
    if number == 1 or number == 0:
        return 1
    else:
        return number * fact(number - 1)


def sum(line, row):
    """
    C (n, k) = n!/(k!(n - k)!)
    n = The current row number (line)
    k = The current column number (row) the current position in the row
    """
    res = fact(line)/(fact(line - row) * fact(row))
    return int(res)
