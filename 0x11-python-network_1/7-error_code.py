#!/usr/bin/python3
""""""
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == '__main__':
    try:
        res = requests(argv[1])
        print(res.__dict__)
    except HTTPError as er:
        print('Error code: {}'.format(er.code))