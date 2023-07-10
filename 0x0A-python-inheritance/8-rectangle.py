#!/usr/bin/python3
"""task 8: this module has a class Rectangle that inherits from
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
