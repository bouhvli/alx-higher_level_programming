#!/usr/bin/python3
"""this model is for finding the peak number"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    debut = 0
    if list_of_integers is None:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    fin = len(list_of_integers) - 1
    while (debut < fin):
        mid = (debut + fin) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1] and
           list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if (list_of_integers[mid] > list_of_integers[mid - 1] and
           list_of_integers[mid] < list_of_integers[mid + 1]):
            return list_of_integers[mid + 1]
        else:
            return max(list_of_integers)
