#!/usr/bin/python3
"""This module has a class called Rectangle
and empty class"""


class Rectangle:
    """This class defines a Rectangle
    Attributes:
        __width (int): the width input value
        __height (int): the height input value
        """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """The getter for the __height

        Returns: (int) the height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height.
        Args:
            value (int): The value that __height will hold
                    if value is == int and > 0
        Attributes:
            __height (int): Private instance attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """The getter for the __width

        Returns: (int) the width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for height.
        Args:
            value (int): The value that __height will hold
                    if value is == int and > 0
        Attributes:
            __height (int): Private instance attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
