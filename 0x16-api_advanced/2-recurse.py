#!/usr/bin/python3
"""
Defines the module ``2-recurse`` which contains the
``recurse`` function.
"""
import requests


API = "https://www.reddit.com/r"
"""Raddit API"""


def recurse(subreddit, hot_list=[], next_page='', count=0):
    """Recursive function that queries the Reddit API
       and returns a list containing the titles of all
       hot articles for a given subreddit.

       Argument:
          subreddit - Raddit group or community.
          next_page - next page to fetch
          count - total number of data fetches

       Returns:
         list of post titles or None.
    """
    req_params = {
        'after': next_page,
        'count': count,
        'limit': 100
    }
    url = "{}/{}/hot.json".format(API, subreddit)

    resp = requests.get(url, params=req_params,
                        headers={"User-agent": "Mozilla/5.0"},
                        allow_redirects=False)

    # Check if request was successfull
    if resp.status_code != requests.codes.ok:
        return (None)

    # Parse res to JSON and return list of all titles
    listing = resp.json().get('data')
    next_page = listing.get('after')  # Get the next page to fetch
    count += len(listing.get('children'))

    # Append all page titles to hot_list
    for child in listing.get('children'):
        hot_list.append(child.get('data').get('title'))

    # Return hot list if no next page
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    return hot_list
