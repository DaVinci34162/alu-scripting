#!/usr/bin/python3
"""Fetches the top 10 hot posts of a given subreddit using Reddit API"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        if data:
            for post in data:
                print(post["data"]["title"])
        else:
            print("None") 
    else:
        print("None")  
