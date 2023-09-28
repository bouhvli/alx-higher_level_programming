#!/usr/bin/python3
"""this model is for finding the peak number"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers is None:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers:
        return max_num(list_of_integers, 0, len(list_of_integers) - 1)
    else:
        return None


def max_num(array, lw, hg):
    """this funtion will look for the max value in the list"""
    if (lw == hg):
        return array[lw]
    mid = (lw + hg) // 2

    if array[mid] > array[mid + 1]:
        return max_num(array, lw, mid)
    else:
        return max_num(array, mid + 1, hg)
