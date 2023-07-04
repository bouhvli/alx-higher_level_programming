#!/usr/bin/python3
"""
This module provide a function that will print a square of #.
Functions:
    - sprint_square: print a square of #
Usage example:
>>> sprint_square = __import__('4-print_square.py').print_square
>>> print_square(5)
#####
#####
#####
#####
#####
"""


def print_square(size):
    """This is the mothode that print the square

    Args:
    size (int): the size of the square input value.

    Prints:
    str :   # * (size cols)
            # * (size lines)
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        i = 0
        j = 0
        while i < size:
            while j < size:
                print("#", end='')
                j += 1
            j = 0
            print()
            i += 1
