#!/usr/bin/python3
"""Function to use API to list top 10 hot posts of a subreddit"""

import ast
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function to get subreddit user count"""
    user_agent = {
     "User-Agent": "Stranger Danger"
    }
    parameters = {
        "limit": 100
    }
    target_url = "https://www.reddit.com/r/" + subreddit\
        + "/hot.json?after=" + str(after)
    r = requests.get(target_url, headers=user_agent, params=parameters,
                     allow_redirects=False)

    if r.status_code == 200:
        hot_post_list = []
        hot_post = r.json().get("data").get("children")
        for post in hot_post:
            hot_list.append(post.get("data").get("title"))
        after = (r.json().get("data").get("after"))
        if after is None:
            return (hot_list)
        return (recurse(subreddit, hot_list, after))
    else:
        return (None)
