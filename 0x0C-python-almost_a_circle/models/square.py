#!/usr/bin/python3
"""this model has the representation of a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this calss is the declaration of the square class and its
    methods"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor for the square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """print hte square dimentions"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def update(self, *args, **kwargs):
        """update the square properties"""
        n = len(args)
        if n > 0:
            if (n >= 1):
                self.id = args[0]
            if (n >= 2):
                self.size = args[1]
            if (n >= 3):
                self.x = args[2]
            if (n >= 4):
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.size = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """preturn a dict that has the square attr"""
        my_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return my_dict
