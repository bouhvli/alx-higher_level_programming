#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last(number):
    if number == 0:
        return 0
    if number < 0:
        number = number * (-1)
    number = number % 10
    return number


if number < 0:
    last = get_last(number) * (-1)
else:
    last = get_last(number)
if last > 5:
    print(
        "Last digit of {} is {} "
        "and is greater than 5".format(number, last)
        )
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
else:
    print(
        "Last digit of {} is {} "
        "and is less than 6 and not 0".format(number, last)
        )
