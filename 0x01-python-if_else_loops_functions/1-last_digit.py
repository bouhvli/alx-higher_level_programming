#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last(number):
    if number == 0:
        return 0
    number = number % 10
    if number < 0:
        number = number * (-1)
    return number


if get_last(number) > 5:
    print(
        "Last digit of {} is {} "
        "and is greater than 5".format(number, get_last(number))
        )
elif get_last(number) < 6 and get_last(number) > 0:
    print(
        "Last digit of {} is {} "
        "and is less than 6 and not 0".format(number, get_last(number))
        )
else:
    print("Last digit of {} is {} and is 0".format(number, get_last(number)))
