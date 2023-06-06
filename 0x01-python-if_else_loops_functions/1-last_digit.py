#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last(number):
    if number == 0:
        return 0
    number = number % 10
    return number


if get_last(number) > 5:
    print(
        f"Last digit of {number: d} is{get_last(number): d} "
        "and is greater than 5"
        )
elif get_last(number) < 6 and get_last(number) > 0:
    print(
        f"Last digit of {number: d} is{get_last(number): d} "
        "and is less than 6 and not 0"
        )
else:
    print(f"Last digit of {number: d} is{get_last(number): d} and is 0")
