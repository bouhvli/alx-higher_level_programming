#!/usr/bin/python3
"""
This module provide a function that divides all elements of a matrix.
Functions:
    - matrix_divided: Returns a new matrix
Usage example:
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    This function perform division on all the matrix elements
    if the matrix is a matrix and each row have the same size,
    and each element or value in the matrix is float or integer,
    and div is != 0 and it is a number
    """
    flag = False
    i = 0
    my_vector = []
    my_matrix = []
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if flag is True:
            if (i != len(row)):
                raise TypeError("Each row of the matrix must have the "
                                "same size")
        else:
            i = len(row)
            flag = True
    for row in matrix:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            res = col / div
            my_vector.append(round(res, 2))
        my_matrix.append(my_vector)
        my_vector = []
    return (my_matrix)
