#!/usr/bin/python3
"""Task 3. Area of a square
in this module we will have a class called Square that
defines a square.
"""


class Square:
    """the square class
    that defines a square by
    Args:
        size (int): the instance attribute
    Attributes:
        __size (int): Private instance attribute

    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """The getter for the __size
        Returnns:
            __size (int): Private instance attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function.
        Args:
            value (int): The value that size will hold
        Attributes:
            __size (int): Private instance attribute
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area function
        Attributes:
            __size (int): the size
        Returns:
            (int): the value of the  the current square area
        """
        return (self.__size * self.__size)
