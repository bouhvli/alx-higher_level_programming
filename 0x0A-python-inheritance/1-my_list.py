#!/usr/bin/python3
"""task 1 about class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """Public instance method: def print_sorted(self):
        that prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
