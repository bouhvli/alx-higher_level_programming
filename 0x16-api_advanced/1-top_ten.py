#!/usr/bin/python3
"""sumary_line
"""
import requests


def top_ten(subreddit):
    """sumary_line
    """
    
    url = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0 (by /u/bouhvli)'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for i, post in enumerate(posts):
                title = post['data']['title']
                print("{}. {}".format(i + 1 - 1, title))
        except(KeyError):
            print("None")
    else:
        print("None")
