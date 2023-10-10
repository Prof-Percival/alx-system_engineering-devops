#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response_data = requests.get(url, headers=headers, allow_redirects=False)
    if response_data.status_code == 404:
        return 0
    results_data = response_data.json().get("data")
    return results_data.get("subscribers")
