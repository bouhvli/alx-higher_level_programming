#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is None:
        return 0
    else:
        my_dict = {key: value for key, value in my_list}
        som = 0
        div = 0
        for key, value in my_dict.items():
            som += key * value
            div += value
        if div == 0:
            return 0
        else:
            return som / div
