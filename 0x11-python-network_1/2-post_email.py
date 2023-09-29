#!/usr/bin/python3
"""
    script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter,and displays the body of the response
    (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email).encode('utf-8')
    reqUrl = Request(url, data=data)
    with urlopen(reqUrl) as res:
        print(res.read().decode('utf-8'))
