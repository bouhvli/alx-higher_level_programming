#!/usr/bin/python3
"""this model has a script that fetches
    https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode('utf-8')))
