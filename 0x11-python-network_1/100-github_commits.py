#!/usr/bin/python3
"""
script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]

    git_res = get('https://api.github.com/repos/{}/{}/commits'
                  .format(owner, repo))
    json = git_res.json()

    try:
        for i in range(10):
            sha = json[i].get('sha')
            name = json[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except IndexError:
        pass
