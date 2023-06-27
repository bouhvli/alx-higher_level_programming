#!/usr/bin/python3
"""10. ByteCode -> Python #5
Write the Python class MagicClass that does exactly
the same as the following Python bytecode
"""
import math


class MagicClass:
    """Class called MagicClass represent the magical
    cercle with radius.
    Attributes:
        __radius (float): the radius.
    """
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """get the area of a circle
        Returns:
            number (float): the result
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """get the circumference of the circle
        Returns:
            number (float): the result
        """
        return 2 * math.pi * self.__radius
