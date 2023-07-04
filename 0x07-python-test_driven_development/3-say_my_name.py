#!/usr/bin/python3
"""
This module provide a function that will print the some info.
Functions:
    - say_my_name: print 'My name is first name last name'
Usage example:
>>> say_my_name = __import__('3-say_my_name').say_my_name
>>> say_my_name("hamza", "bouhali")
My name is hamza bouhali
"""


def say_my_name(first_name, last_name=""):
    """This is the mothode that print the string

    Args:
    first_name (str): the input string for the first name.
    last_name (str): the input string for the last name.

    Prints:
    str : My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    for i in first_name:
        if i.isdigit() or i == " ":
            raise TypeError("first_name must be a string")
    for i in last_name:
        if i.isdigit() or i == " ":
            raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
