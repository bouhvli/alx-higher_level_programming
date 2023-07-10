#!/usr/bin/python3
"""task 9: this module has a class Rectangle that inherits from
BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)."""
    def __init__(self, width, height):
        """the constructor with a checker for the values"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """overrding the Public instance method: def area(self): that
        raises an Exception with the message area() is not
        implemented"""
        return self.__height * self.__width

    def __str__(self):
        """str() will return, the following rectangle
        description: [Rectangle] <width>/<height>"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
