#!/usr/bin/python3
"""This module has a class called Rectangle
and empty class"""


class Rectangle:
    """This class defines a Rectangle
    Attributes:
        __width (int): the width input value
        __height (int): the height input value
        number_of_instances (int): Public class attribute.
        print_symbol (*): the symbole to print the rectangle with.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
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
                    string += str(self.print_symbol)
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

    def bigger_or_equal(rect_1, rect_2):
        """
        a function that returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): the first rectangle.
            rect_2 (Rectangle): the second rectangle.

        Returns:
            (Rectangle): the biggest and if they are equal return the first
            rect_1.
        """
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (type(rect_2) != Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class method def square(cls, size=0): that returns a new
        Rectangle instance with width == height == size

        Args:
            size (int): the size of the rectagle.

        Returns:
            (Rectangle): rectangle with the given size.
        """
        return Rectangle(size, size)
