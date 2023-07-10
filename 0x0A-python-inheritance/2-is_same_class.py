#!/usr/bin/python3
"""task 2 has a mothode caled is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class  a function that returns
    True if the object is exactly an instance of the
    specified class ; otherwise False."""
    return type(obj) is a_class
