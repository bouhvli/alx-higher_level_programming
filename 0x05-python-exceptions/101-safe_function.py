#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as joy:
        print("Exception: {}".format(joy), file=sys.stderr)
        return (None)
    return (res)
