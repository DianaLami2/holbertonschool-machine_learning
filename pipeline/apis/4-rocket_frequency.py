import requests
from collections import defaultdict

def get_launch_data():
    # Fetch data from the SpaceX API
    response = requests.get("https://api.spacexdata.com/v4/launches")
    if response.status_code != 200:
        raise Exception("Failed to fetch data from SpaceX API.")
    
    return response.json()

def count_launches_by_rocket(launch_data):
    rocket_launch_count = defaultdict(int)
    
    # Count launches per rocket
    for launch in launch_data:
        rocket_id = launch['rocket']
        rocket_launch_count[rocket_id] += 1
    
    return rocket_launch_count

def get_rocket_names():
    # Fetch rocket names from the SpaceX API
    response = requests.get("https://api.spacexdata.com/v4/rockets")
    if response.status_code != 200:
        raise Exception("Failed to fetch rocket data from SpaceX API.")
    
    rockets_data = response.json()
    return {rocket['id']: rocket['name'] for rocket in rockets_data}

def display_rocket_launches(rocket_launch_count, rocket_names):
    # Create a list of tuples (rocket_name, launch_count) and sort it as per requirements
    launches_per_rocket = [(rocket_names[rocket_id], count) for rocket_id, count in rocket_launch_count.items()]
    launches_per_rocket.sort(key=lambda x: (-x[1], x[0]))

    # Print the result in the desired format
    for rocket_name, count in launches_per_rocket:
        print(f"{rocket_name}: {count}")

if __name__ == '__main__':
    launch_data = get_launch_data()
    rocket_launch_count = count_launches_by_rocket(launch_data)
    rocket_names = get_rocket_names()
    display_rocket_launches(rocket_launch_count, rocket_names)
    