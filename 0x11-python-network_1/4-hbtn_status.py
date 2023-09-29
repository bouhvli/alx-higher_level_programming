#!/usr/bin/python3
"""
    script that fetches https://alx-intranet.hbtn.io/status
    using the package requests
"""
import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.content.decode('utf-8'))))
    print('\t- content: {}'.format(res.content.decode('utf-8')))
