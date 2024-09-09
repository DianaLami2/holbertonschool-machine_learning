#!/usr/bin/env python3
"""Pipeline Api"""

import requests
import sys
import time

def get_user_location(url):
    """Get the location of a GitHub user"""
    response = requests.get(url)
    
    if response.status_code == 200:
        location = response.json().get('location')
        if location:
            print(location)
        else:
            print("Not found")
    elif response.status_code == 403:
        reset_time = response.headers.get('X-Ratelimit-Reset')
        if reset_time:
            reset_in = int(reset_time) - int(time.time())
            minutes = reset_in // 60
            print(f"Reset in {minutes} min")
        else:
            print("Rate limit exceeded")
    else:
        print("Not found")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python 2-user_location.py <github_api_url>")
        sys.exit(1)

    url = sys.argv[1]
    get_user_location(url)
    