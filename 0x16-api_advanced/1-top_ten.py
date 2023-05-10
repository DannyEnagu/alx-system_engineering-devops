#!/usr/bin/python3
"""
Defines the module ``1-top_ten`` which contains the
``top_ten.py`` function.
"""
import requests


URL = "https://www.reddit.com/r"
"""Raddit API"""


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
       the 10 hot posts listed for a given subreddit.

       Argument:
          subreddit - Raddit group or community.

       Prints:
         list of post titles or None.
    """
    resp = requests.get("{}/{}/hot.json?limit=10".format(URL, subreddit),
                        headers={"User-agent": "Mozilla/5.0"},
                        allow_redirects=False)

    # Check if request was successfull
    if resp.status_code != requests.codes.ok:
        print(None)
    else:
        # Parse res to JSON and return number of subcribers
        for res in resp.json().get('data').get('children'):
            print(res.get('data').get('title'))
