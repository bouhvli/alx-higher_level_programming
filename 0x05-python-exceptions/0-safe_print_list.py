#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numberOfElements = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            numberOfElements += 1
    except (IndexError, TypeError):
        pass
    print()
    return (numberOfElements)
