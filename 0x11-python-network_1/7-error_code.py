#!/usr/bin/python3
""""""
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == '__main__':
    try:
        res = requests(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as er:
        print('Error code: {}'.format(er.code))