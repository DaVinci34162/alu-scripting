#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}
    
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    
    if not posts:
        print(None)
        return
    
    for post in posts[:10]:
        print(post['data']['title'])
