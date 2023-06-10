#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    up_list = []
    for i in my_list:
        if i.upper() != 'C':
            up_list.append(i)
    new_string = ''.join(up_list)
    return (new_string)
