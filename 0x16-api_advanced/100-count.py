#!/usr/bin/python3
"""
Defines the module ``100-count`` which contains the
``count_words`` function.
"""
import requests


API = "https://www.reddit.com/r"
"""Raddit API"""


def count_words(subreddit, word_list=[], found={}, next_page=None, count=0):
    """Recursive function that queries the Reddit API,
       parses the title of all hot articles, and prints
       a sorted count of given keywords.

       Argument:
          word_list (list) - list of keywords to search for
          found (dict) - dictionary of all keywords count.
          subreddit (str) - Raddit group or community.
          next_page (str)- next page to fetch
          count (str)- total number of data fetches

       prints:
         Each keyword and number of occurance or Nothing.
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

    if next_page is None:
        word_list = [w.lower() for w in word_list]
        found = {x: 0 for x in sorted(word_list)}

    # Check if request was successfull
    if resp.status_code == requests.codes.ok:
        # Parse res to JSON and update count
        listing = resp.json().get('data')
        next_page = listing.get('after')  # Get the next page to fetch
        count += len(listing.get('children'))

        # Update keyword count if found in post title
        for child in listing.get('children'):
            title = child.get('data').get('title').lower()
            for word in title.split():
                if word in word_list:
                    found[word] += 1

        # Continue is next page is found
        if next_page is not None:
            count_words(subreddit, word_list, found, next_page, count)
        else:
            found = sorted(found.items(), key=lambda x: x[1], reverse=True)
            found = dict(found)
            for key in found:
                if found[key] != 0:
                    print("{}: {}".format(key, found[key]))
