#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, allow_redirects=False, headers={
                        'User-agent': 'erika hbtn 1.0'})
    if resp.ok:
        results = resp.json().get("data")
        return results.get("subscribers")
    return 0
