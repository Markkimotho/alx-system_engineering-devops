#!/usr/bin/python3
"""Module that queries reddit API for its total subs
"""

import requests


def number_of_subscribers(subreddit):
    """Functions that returns number of subreddit subs
    Args: subreddit - subreddit to be queried
    """
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "0x16. API advanced"
    headers = {"User-Agent": user_agent}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    subscribers = response.json()["data"]["subscribers"]

    return subscribers
