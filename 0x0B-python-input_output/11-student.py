#!/usr/bin/python3
"""
Task 11: Student to disk and reload
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
        """ retrieves a dictionary representation of a Student instance"""
        json_dict = {}
        if attrs is None:
            attrs = []
            return self.__dict__
        for key in self.__dict__.keys():
            if key in attrs:
                json_dict[key] = self.__dict__[key]
        return json_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
