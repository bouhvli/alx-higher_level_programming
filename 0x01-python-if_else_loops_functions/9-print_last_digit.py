#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = number * (-1)
        last = n % 10
    else:
        last = number % 10
    print(f"{last :d}", end='')
    return last
