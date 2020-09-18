#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords"""

import requests


def count_words(subreddit, word_list, result_dict={}, after=""):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {
        'limit': 100,
        'after': after
    }
    resp = requests.get(url, allow_redirects=False, headers={
        'User-agent': 'erika hbtn 1.0'}, params=parameters)

    if resp.ok:
        try:
            result = resp.json().get('data')
            after = result.get('after')
            new_list = result.get('children')
            for post in new_list:
                title = post.get('data').get('title').lower().split()
                for word in word_list:
                    if word.lower() in title:
                        result_dict[word] = result_dict.get(word, 0) + 1
            if after is None:
                for k in sorted(result_dict, key=result_dict.get,
                                reverse=True):
                    print("{}: {}".format(k, result_dict[k]))
                return
            return count_words(subreddit, word_list, result_dict, after)
        except:
            pass
    print()
    return
