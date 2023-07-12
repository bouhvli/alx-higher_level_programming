#!/usr/bin/python3
"""
Task 8: Class to JSON
"""


def class_to_json(obj):
    """a function that returns the dictionary description
    with simple data structure
    for JSON serialization of an object"""
    if (isinstance(obj, (list, tuple))):
        return [class_to_json(idx) for idx in obj]
    elif (isinstance(obj, (str, int, bool))):
        return obj
    elif (isinstance(obj, dict)):
        return {class_to_json(key): class_to_json(value) for
                key, value in obj.items()}
    elif (hasattr(obj, '__dict__')):
        return class_to_json(obj.__dict__)
    else:
        return (None)
