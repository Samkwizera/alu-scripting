#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit.
    If subreddit is invalid, print None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit exists
        if response.status_code != 200:
            print(None)
            return

        # Parse JSON data
        data = response.json().get('data', {})
        posts = data.get('children', [])
        
        # Print up to 10 post titles
        for i in range(min(10, len(posts))):
            title = posts[i].get('data', {}).get('title')
            if title:
                print(title)
                
    except Exception as e:
        print(None)
