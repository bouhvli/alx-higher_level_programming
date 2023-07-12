#!/usr/bin/python3
"""
Task 10: Student to JSON with filter
"""


class Student:
    """
    class Student that defines a student by:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
