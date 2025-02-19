#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 404:
            print("None")
            return
            
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print("None")
                return
                
            for post in posts[:10]:
                print(post.get('data', {}).get('title', ''))
        else:
            print("None")
            
    except Exception:
        print("None")
