#!/usr/bin/python3
"""Module to query Reddit API and print titles of first 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit: string, the name of the subreddit
    
    Prints:
        The titles of the first 10 hot posts, or None if subreddit is invalid
    """
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'linux:1-top_ten:v1.0.0 (by /u/your_username)'
    }

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful and subreddit exists
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json()['data']['children']
            
            # Print the title of each post
            for post in posts:
                print(post['data']['title'])
        else:
            # Subreddit not found or other error
            print(None)

    except Exception:
        # Handle any errors that occur during the request
        print(None)
