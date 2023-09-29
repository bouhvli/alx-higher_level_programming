#!/usr/bin/python3
"""
script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id.
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    token = argv[2]
    user = argv[1]
    login = HTTPBasicAuth(user, token)

    git_res = get('https://api.github.com/user', auth=login)
    json = git_res.json()
    print(json.get('id'))
