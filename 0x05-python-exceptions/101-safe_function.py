#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    var1, var2 = args
    try:
        res = fct(var1, var2)
    except ValueError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (None)
    except TypeError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (None)
    except IndexError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (None)
    except ZeroDivisionError as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (None)
    return (res)
