#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
Usage: python3 1-main.py programming
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    resp = requests.get(url, allow_redirects=False, headers={
                        'User-agent': 'erika hbtn 1.0'})
    if resp.ok:
        lista = resp.json().get('data').get('children')[:10]
        for post in lista:
            print(post.get('data').get('title'))
    print(None)
    return (0)
