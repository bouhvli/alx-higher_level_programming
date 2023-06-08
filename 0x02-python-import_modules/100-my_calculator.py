#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def switch(a, operator, b):
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    args = sys.argv[1:]
    lenargvs = len(args)
    if lenargvs == 0 or lenargvs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        switch(int(args[0]), args[1], int(args[2]))
