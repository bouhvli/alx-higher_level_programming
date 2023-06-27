#!/usr/bin/python3
"""Task 3. Area of a square
in this module we will have a class called Square that
defines a square.
"""


class Square:
    """the square class
    that defines a square by
    Args:
        size (int): the instance attribute
        position (tuple): the instance attribute
    Attributes:
        __size (int): Private instance attribute
        __position (tuple): Private instance attribute

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """The getter for the __size
        Returnns:
            __size (int): Private instance attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function for size.
        Args:
            value (int): The value that size will hold
        Attributes:
            __size (int): Private instance attribute
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """The getter for the __position
        Returnns:
            __position (tuple): Private instance attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter function for position.
        Args:
            value (tuple): The value that position will hold
        Attributes:
            __position (tuple): Private instance attribute
        """
        if ((type(value) != tuple) and (value[0] < 0) and
                (value[1] < 0) and (len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area function
        Attributes:
            __size (int): the size
        Returns:
            (int): the value of the  the current square area
        """
        return (self.__size * self.__size)

    def representation_str(self):
        string = ''
        if (self.__size == 0):
            string += "\n"
        else:
            i = 0
            j = 0
            while (i < self.__position[1]):
                string += "\n"
                i += 1
            i = 0
            while (i < self.__size):
                while (j < self.__position[0]):
                    string += " "
                    j += 1
                j = 0
                while (j < self.__size):
                    string += "#"
                    j += 1
                j = 0
                string += "\n"
                i += 1
        if string.endswith("\n"):
            return string[:-1]
        return string

    def my_print(self):
        """print # to form a square based on the size.
        Attributes:
            __size (int): the size
            __position (tuple): the tuple
        """
        print(self.representation_str(), end="")

    def __str__(self):
        return self.representation_str()
