#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def func(ln):
        return ln * number
    new_list = list(map(func, my_list))
    return new_list
