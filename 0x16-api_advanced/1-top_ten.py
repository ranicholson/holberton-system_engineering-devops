#!/usr/bin/python3
"""Function to use API to list top 10 hot posts of a subreddit"""

import requests


def top_ten(subreddit):
    """Function to get subreddit user count"""
    user_agent = {
     "User-Agent": "Stranger Danger"
    }
    parameters = {
        "limit": 10
    }
    target_url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    r = requests.get(target_url, headers=user_agent, params=parameters)

    if r.status_code == 200:
        hot_post = r.json().get("data").get("children")
        for post in hot_post:
            print(post.get("data").get("title"))
    return (0)
