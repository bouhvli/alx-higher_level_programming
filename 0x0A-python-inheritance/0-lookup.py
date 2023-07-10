#!/usr/bin/python3
"""task 0 about the creating a function that returuns a
list of objects"""


def lookup(obj):
    """Lookup is a function that returns the
    list of available attributes and methods of an object
    Returns a list object"""
    return (dir(obj))
