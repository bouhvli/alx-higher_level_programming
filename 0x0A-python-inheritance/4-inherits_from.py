#!/usr/bin/python3
"""task 4 has a mothode caled inherits_from
"""


def inherits_from(obj, a_class):
    """inherits_from  a function that returns True if the
    object is an instance of a class that inherited (directly or
    indirectly) from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
