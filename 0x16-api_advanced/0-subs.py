#!/usr/bin/python3
"""sumary_line
"""
import requests


def number_of_subscribers(subreddit):
    """sumary_line
    """
    
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        res = response.json()["data"]["subscribers"]
        return res
    return (0)
