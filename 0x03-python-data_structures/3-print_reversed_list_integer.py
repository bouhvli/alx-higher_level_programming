#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    new_list = my_list[::-1]
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
