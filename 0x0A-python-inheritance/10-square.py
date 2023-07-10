#!/usr/bin/python3
"""task 10: this module has a class Square that inherits from
Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class Square that inherits from Rectangle
    (9-rectangle.py)"""
    def __init__(self, size):
        """the constructor for the square class this will
        validate the number"""
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """overrding the Public instance method: def area(self): that
        raises an Exception with the message area() is not
        implemented"""
        return (self.__size * self.__size)
