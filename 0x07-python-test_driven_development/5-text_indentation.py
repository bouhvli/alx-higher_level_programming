#!/usr/bin/python3
"""
    This module provide a function that rints a text with 2 new lines after
    each of these characters:" ., ? and :".
    Functions:
        - sprint_square: print the text input based on the condition mentioned.
    Usage example:
    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("hamza?bouhali. new line:")
    hamza?
    <BLANKLINE>
    bouhali.
    <BLANKLINE>
    new line:
    <BLANKLINE>
"""


def text_indentation(text):
    """This is the mothode prints a text with 2 new lines after
    ., ? and :

    Args:
    text (str): the input text must be string format.

    Prints:
    str :   the formated text.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        regix = ['?', '.', ':']
        back = False
        for i in text:
            if i in [' ', "\t"] and back is True:
                continue
            else:
                print(i, end='')
                back = False
            if i in regix:
                print(end="\n\n")
                back = True
