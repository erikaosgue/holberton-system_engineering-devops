#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
Usage: python3 2-main.py programming"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {
        'limit': 100,
        'after': after
    }
    resp = requests.get(url, allow_redirects=False, headers={
        'User-agent': 'erika hbtn 1.0'}, params=parameters)

    if resp.ok:
        result = resp.json().get('data')
        after = result.get('after')
        new_list = result.get('children')

        for post in new_list:
            hot_list.append(post.get('data').get('title'))
        if after is None:
            return(hot_list)
        return recurse(subreddit, hot_list, after)
