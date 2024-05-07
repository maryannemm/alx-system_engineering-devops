#!/usr/bin/python3
"""
Reddit API: Recursive Query
"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")

