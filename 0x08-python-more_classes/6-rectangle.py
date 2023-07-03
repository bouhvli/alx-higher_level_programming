#!/usr/bin/python3
"""This module has a class called Rectangle
and empty class"""


class Rectangle:
    """This class defines a Rectangle
    Attributes:
        __width (int): the width input value
        __height (int): the height input value
        number_of_instances (int): Public class attribute.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """
        This function 'area':
        claculate the area of a rectangle.

        Returns:
            (int) the result of (height * width)
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        This function 'perimeter':
        claculate the perimeter of a rectangle.

        Returns:
            (int) the result of 2 * (height + width)
        """
        if self.__height == 0 or self.width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def rec(self):
        """
        This function will return a string for __str__:
        based on the height and width this function will create
        a rectangle and return it in string format.

        Attributes:
            __height (int): the height of the rectagle.
            __width (int): the width of the rectangle.

        Returns:
            (str): the rectangle based on the height and width
        """
        string = ""
        if self.__height == 0 or self.width == 0:
            return (string)
        else:
            h = 0
            w = 0
            while (h < self.__height):
                while (w < self.__width):
                    string += "#"
                    w += 1
                w = 0
                h += 1
                if (h != self.__height):
                    string += "\n"
            return (string)

    def __str__(self):
        return (self.rec())

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
