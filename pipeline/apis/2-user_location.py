#!/usr/bin/env python3
"""
A script to print the location of a specific GitHub user using the GitHub API.
The user is passed as the first argument of the script with the full API URL.

Usage:
    ./2-user_location.py <GitHub API URL>

Example:
    ./2-user_location.py https://api.github.com/users/holbertonschool
"""

import requests
import sys
from datetime import datetime


def get_user_location(api_url):
    """
    Fetches and prints the location of a GitHub user from the given API URL.

    Args:
        api_url (str): The URL of the GitHub API for a specific user.

    Returns:
        None
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get('location', 'Location not available')
            print(location)
        elif response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            # Retrieve the rate limit reset time from the response headers
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            # Calculate the time difference in minutes
            reset_minutes = (reset_time - int(datetime.now().timestamp())) // 60
            print(f"Reset in {reset_minutes} min")
        else:
            print(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    get_user_location(api_url)
