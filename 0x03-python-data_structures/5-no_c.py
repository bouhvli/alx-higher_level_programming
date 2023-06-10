#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    up_list = []
    if (my_list.count('c') != 0 or my_list.count('C') != 0):
        for i in my_list:
            if i.upper() != 'C':
                up_list.append(i)
            else:
                continue
        new_string = ''.join(up_list)
        return (new_string)
