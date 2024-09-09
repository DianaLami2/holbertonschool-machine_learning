#!/usr/bin/env python3
"""
A script to display the first launch from SpaceX API with specific details.
"""

import requests

def get_first_launch():
    """Fetches and displays the first launch details using SpaceX API."""
    url = "https://api.spacexdata.com/v4/launches"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        launches = response.json()

        # Sorting launches by date (using `date_unix`) in ascending order
        sorted_launches = sorted(launches, key=lambda x: x['date_unix'])
        first_launch = sorted_launches[0]

        # Extract necessary information
        launch_name = first_launch['name']
        launch_date = first_launch['date_local']
        rocket_id = first_launch['rocket']
        launchpad_id = first_launch['launchpad']

        # Fetch rocket name
        rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        rocket_name = requests.get(rocket_url).json().get('name')

        # Fetch launchpad name and locality
        launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        launchpad_info = requests.get(launchpad_url).json()
        launchpad_name = launchpad_info.get('name')
        launchpad_locality = launchpad_info.get('locality')

        # Print the formatted result
        print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

    except requests.RequestException as e:
        print(f"Error fetching data from SpaceX API: {e}")

if __name__ == "__main__":
    get_first_launch()
