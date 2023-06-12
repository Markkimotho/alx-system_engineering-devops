#!/usr/bin/python3
"""Module that queries a subreddit for hot topics and returns the count
of a given set of words parse as terminal arguments
"""

import requests


def count_words(subreddit, word_list):
    """Recursive function that returns how many times a word appears
    in a subreddit's hot title
    """
