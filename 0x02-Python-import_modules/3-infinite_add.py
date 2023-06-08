#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    lenlist = len(arguments)
    if lenlist == 0:
        print("0")
    else:
        i = 0
        sum = 0
        while i < len(arguments):
            sum = sum + int(arguments[i])
            i += 1
        print(sum)
