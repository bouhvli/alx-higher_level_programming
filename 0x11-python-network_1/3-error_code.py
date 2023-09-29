#!/usr/bin/python3
""""""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            print(res)
    except HTTPError as er:
        print(er.code)