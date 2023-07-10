#!/usr/bin/python3
"""task 3 has a mothode caled dis_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class a function that returns True if the object
    is an instance of, or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False."""
    return isinstance(obj, a_class)
