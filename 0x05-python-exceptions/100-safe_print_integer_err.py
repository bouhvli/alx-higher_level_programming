#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value));
    except ValueError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (False);
    except TypeError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (False);
    return (True);