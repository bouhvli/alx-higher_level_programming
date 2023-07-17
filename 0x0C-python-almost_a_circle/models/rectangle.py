#!/usr/bin/python3
"""this module has the representation of the Rectangle madel"""
from models.base import Base
import json


class Rectangle(Base):
    """this calss is the declaration of the rectangle class and its
    methods"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """this method calc the area"""
        return self.width * self.height

    def display(self):
        """this method print the rectangle"""
        output = ""
        for k in range(self.y):
            output += "\n"
        for i in range(self.height):
            for lo in range(self.x):
                output += " "
            for j in range(self.width):
                output += "#"
            output += "\n"
        print(output, end="")
        return (output)

    def __str__(self):
        """this method present the Rectangle dimentions"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """this method update the properties of a reac"""
        n = len(args)
        if n > 0:
            if (n >= 1):
                self.id = args[0]
            if (n >= 2):
                self.width = args[1]
            if (n >= 3):
                self.height = args[2]
            if (n >= 4):
                self.x = args[3]
            if (n >= 5):
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "width" in kwargs:
                self.width = kwargs.get("width")
            if "height" in kwargs:
                self.height = kwargs.get("height")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """this function return the rect
        properties in a dict format"""
        my_dict = {
            'id': self.id,
            'height': self.height,
            'width': self.width,
            'x': self.x,
            'y': self.y
        }
        return my_dict
