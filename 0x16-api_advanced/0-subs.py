#!/usr/bin/python3
"""
Defines the module ``0-subs`` which contains the
``number_of_subscribers`` function.
"""
import requests

URL = "https://www.reddit.com/r"
"""Raddit API"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
       (not active users, total subscribers) for a given subreddit.

       Argument:
          subreddit - Raddit group or community.

       Returns:
         Number of subraddit subcriber or 0.
    """
    res = requests.get("{}/{}/about.json".format(URL, subreddit),
                       headers={"User-agent": "Mozilla/5.0"},
                       allow_redirects=False)

    # Check if request was successfull
    if res.status_code != requests.codes.ok:
        return (0)

    # Parse res to JSON and return number of subcribers
    return res.json().get('data').get('subscribers')
