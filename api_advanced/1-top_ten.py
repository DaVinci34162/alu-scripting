#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """API"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
