#!/usr/bin/python3
"""
Task 2. Append to a file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)
        return (len(text))
