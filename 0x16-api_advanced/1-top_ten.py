#!/usr/bin/python3
"""Module that queries for the top 10 hot posts titles
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

    post_titles = []  # List to store post titles

    after = None  # Variable to track the "after" value for pagination

    while len(post_titles) < 10:  # Fetching a total of 10 posts
        url = base_url
        if after:
            # Append "after" parameter for pagination
            url += "&after={}".format(after)

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            raise Exception("None")
        data = response.json()["data"]
        comments = data["children"]
        for comment in comments:
            title = comment["data"]["title"]
            post_titles.append(title)

        after = data["after"]  # Update "after" value for the next page

        if not after:
            break  # Break the loop if there are no more pages

    for title in post_titles:
        print(title)
