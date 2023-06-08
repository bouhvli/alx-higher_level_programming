#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    lenlist = len(arguments)
    if lenlist == 0:
        print("0 argument.")
    else:
        if (lenlist == 1):
            print("{} argument:".format(lenlist))
        else:
            print("{} arguments:".format(lenlist))
        i = 0
        while i < len(arguments):
            print("{}: {}".format(i+1, arguments[i]))
            i += 1
