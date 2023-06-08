#!/usr/bin/python3
"""
Module that queries for the top 10 hot posts titles
from a subreddit using the reddit API
"""

import requests


def top_ten(subreddit):
    """Function that returns the top 10 hottest topics
    of a subreddit
    Args: subreddit - subreddit to be queries
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    user_agent = "0x16. API advanced"
    headers = {"User-Agent": user_agent}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)

    elif response.status_code == 302:
        print("None")
