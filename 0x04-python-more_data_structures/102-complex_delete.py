#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for key, data in a_dictionary.items():
        if data == value:
            my_list.append(key)
    if len(my_list) != 0:
        for elem in my_list:
            del a_dictionary[elem]
    return a_dictionary
