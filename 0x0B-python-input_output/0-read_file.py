#!/usr/bin/python3
"""
Task 0: read file and print it
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints
    it to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
