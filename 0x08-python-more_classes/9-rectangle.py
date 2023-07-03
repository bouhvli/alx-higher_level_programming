#!/usr/bin/python3
"""This module has a class called Rectangle
and empty class"""


class Rectangle:
    """This class defines a Rectangle
        __width (int): the width input value
        __height (int): the height input value
        number_of_instances (int): Public class attribute.
        print_symbol (*): the symbole to print the rectangle with.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def rec(self):
        string = ""
        if self.__height == 0 or self.width == 0:
            return (string)
        else:
            h = 0
            w = 0
            while (h < self.__height):
                while (w < self.__width):
                    string += str(self.print_symbol)
                    w += 1
                w = 0
                h += 1
                if (h != self.__height):
                    string += "\n"
            return (string)

    def __str__(self):
        return (self.rec())

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (type(rect_2) != Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1
