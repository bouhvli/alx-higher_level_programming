#!/usr/bin/python3
"""
This module provide a function that will add two integers
Functions:
    - add_integer: Returns an integer: the addition of a and b
Usage example:
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    This function perform the addition of two integers, if
    they are floats it will convert them into integers.

    Args:
    a (int, float): the first input value.
    b (int, float): the second input value.

    Returns:
    int : the result of the addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            vala = int(a)
        else:
            vala = a
        if type(b) is float:
            valb = int(b)
        else:
            valb = b
    return vala + valb
