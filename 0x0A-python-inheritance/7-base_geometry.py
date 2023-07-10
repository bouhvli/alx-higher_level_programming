#!/usr/bin/python3
"""task 6 has a class called BaseGeometry
"""


class BaseGeometry:
    """this class has a method that calculate the area
    and has a checker for the input values integer_validator"""
    def area(self):
        """Public instance method: def area(self): that
        raises an Exception with the message area() is not
        implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def
        integer_validator(self, name, value): that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
