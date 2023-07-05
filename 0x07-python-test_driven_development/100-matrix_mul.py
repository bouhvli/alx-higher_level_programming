#!/usr/bin/python3
"""The matrix_mul module has a method matrix_mul
    matrix_mul = __import__('100-matrix_mul').matrix_mul"""


def check_error(matrix, tp_er, ll_er, sz_er, em_er):
    for row in matrix:
        if type(row) is not list:
            raise TypeError(ll_er)
        if (len(row) != len(matrix[0])):
            raise ValueError(sz_er)
        if (len(row) == 0):
            raise ValueError(em_er)
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(tp_er)


def matrix_mul(m_a, m_b):
    """this is a function that multiplies 2 matrices
    m_a and m_b must be validated with the requirements"""
    list_error = ["m_a must be a list", "m_b must be a list"]
    ll_error = ["m_a must be a list of lists",
                "m_b must be a list of lists"]
    empty_error = ["m_a can't be empty", "m_b can't be empty"]
    type_error = ["m_a should contain only integers or floats",
                  "m_b should contain only integers or floats"]
    size_error = ["each row of m_a must be of the same size",
                  "each row of m_b must be of the same size"]
    mul_error = "m_a and m_b can't be multiplied"

    if (type(m_a) is not list):
        raise TypeError(list_error[0])
    if (type(m_b) is not list):
        raise TypeError(list_error[1])
    if (len(m_a) == 0):
        raise ValueError(empty_error[0])
    if (len(m_b) == 0):
        raise ValueError(empty_error[1])

    check_error(m_a, type_error[0], ll_error[0],
                size_error[0], empty_error[0])
    check_error(m_b, type_error[1], ll_error[1],
                size_error[1], empty_error[1])

    m = len(m_a)
    n = len(m_a[0])
    p = len(m_b[0])

    if len(m_b) != n:
        raise ValueError(mul_error)

    C = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += (m_a[i][k] * m_b[k][j])

    return C
