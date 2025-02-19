#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the top 10 hot post titles for a given subreddit."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    response = requests.get(subreddit_url, headers=headers, params={'limit': 10}, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title', 'No title found'))
    else:
        print(None)

