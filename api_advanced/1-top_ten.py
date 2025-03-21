#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """API"""
   url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
