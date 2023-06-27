#!/usr/bin/python3
"""Task 2. Size validation
in this module we will have a class called Square that
defines a square.
"""


class Square:
    """the square class
    that defines a square by
    Attributes:
        size : Private instance attribute
    Raises:
        TypeError: if size is not an number(int)
        ValueError: if size < 0
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
