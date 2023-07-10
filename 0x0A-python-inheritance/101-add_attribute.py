#!/usr/bin/python3
"""task 13: this module has a method called add_attribute"""


def add_attribute(obj, name, value):
    """ a function that adds a new attribute to
    an object if it's possible Raise a TypeError exception,
    with the message can't add new attribute if the object
    can't have new attribute"""
    if (hasattr(obj, "__dict__")):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
