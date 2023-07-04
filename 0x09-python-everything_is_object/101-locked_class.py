#!/usr/bin/python3
"""This module has a class called LockedClass"""


class LockedClass:
    """This class LockedClass with no class or object attribute
    prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name.
    """
    __slots__ = ['first_name']
