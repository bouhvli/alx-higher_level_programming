#!/usr/bin/python3
"""Task 13: Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r", encoding="UTF-8") as file:
        text = file.readlines()
    with open(filename, "w", encoding="utf-8") as file:
        for line in text:
            file.write(line)
            if (search_string in line):
                file.write(new_string)
