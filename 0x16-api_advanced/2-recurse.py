#!/usr/bin/python3
"""Module that queries the reddit API to fetch comments recursively
"""

import requests


def recurse(subreddit, hot_list=None):
    """Recursive function that returns a list of subreddit's
    hot topics' titles
    Args:   subreddit - subreddit to be queried
            hot_list[]- list to returned
    """
    if hot_list is None:
        hot_list = []

    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "0x16. API advanced"
    headers = {"User-Agent": user_agent}

    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        raise Exception("None")

    data = response.json()["data"]
    comments = data["children"]
    for comment in comments:
        title = comment["data"]["title"]
        hot_list.append(title)

    after = data["after"]

    if after:
        return recurse(subreddit, hot_list=hot_list)

    return hot_list
