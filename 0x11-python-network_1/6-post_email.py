#!/usr/bin/python3
"""
    script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email
    as a parameter, and finally displays the body of the response
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    res = requests.post(url, data=email)
    print(res._content.decode('utf-8'))
