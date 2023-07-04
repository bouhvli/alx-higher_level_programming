#!/usr/bin/python3
"""This module has a class called LockedClass"""


class LockedClass:
    """This class LockedClass with no class or object attribute
    prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name.
    """
    def __init__(self):
        self.first_name = None

    def __setattr__(self, __name: str, __value):
        if __name == "first_name" or hasattr(self, __name):
            object.__setattr__(self, __name, __value)
        else:
            raise AttributeError("'LockedClass' object has "
                                 "no attribute '{}'".format(__name))
