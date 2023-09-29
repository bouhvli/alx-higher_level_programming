#!/usr/bin/python3
"""
    script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    if argv[2]:
        data = {'q': argv[2]}
    else:
        data = {'q': ""}

    res = requests.get(url, data=data)
    json = res._content.decode('utf-8')

    if (len(json)):
        if (isinstance(json, dict)):
            key, value = json.values()
            print('[{}] {}'.format(key, value))
        else:
            print('Not a valid JSON')
    else:
        print('No result')
