#!/usr/bin/python3
"""
Multiply matrix using the numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ lazy mul using num py """
    try:
        new_mat = numpy.dot(m_a, m_b)
        return new_mat
    except Exception as e:
        print("{}".format(e))
