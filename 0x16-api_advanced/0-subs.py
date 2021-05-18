#!/usr/bin/python3
"""Function to use API to get user count of subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function to get subreddit user count"""
    user_agent = {
     "User-Agent": "Stranger Danger"
    }
    target_url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    r = requests.get(target_url, headers=user_agent)

    if r.status_code == 200:
        user_count = r.json().get("data").get("subscribers")
        return (user_count)
    return (0)
