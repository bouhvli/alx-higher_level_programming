#!/usr/bin/python3
"""
    script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    res = requests.post(url, data=data)
    json = res._content.decode('utf-8')

    if (len(json)):
        if (isinstance(json, str)):
            json = eval(json)
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('Not a valid JSON')
    else:
        print('No result')
