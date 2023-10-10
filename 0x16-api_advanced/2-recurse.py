#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response_data = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response_data.status_code == 404:
        return None

    results_data = response_data.json().get("data")
    after = results_data.get("after")
    count += results_data.get("dist")
    for c in results_data.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
