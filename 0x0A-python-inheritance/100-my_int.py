#!/usr/bin/python3
"""task 12: this module has a class called MyInt"""


class MyInt(int):
    """the  class MyInt that inherits from int
    MyInt has == and != operators inverted"""
    def __eq__(self, __value: object) -> bool:
        """the __eq__ is over ride to perform a diffrent
        way of work instead of == this will perform a !="""
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """the __ne__ is over ride to perform a diffrent
        way of work instead of != this will perform a =="""
        return super().__eq__(__value)
