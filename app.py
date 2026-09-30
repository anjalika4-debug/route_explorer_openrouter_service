import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ORS_API_KEY")

# Function to convert place name into coordinates
def get_coordinates(place):
    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "text": place
    }

    headers = {
        "Authorization": api_key
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    data = response.json()

    if len(data["features"]) == 0:
        return None

    coordinates = data["features"][0]["geometry"]["coordinates"]

    return coordinates



# User input
start_place = input("Enter starting place: ")
end_place = input("Enter destination place: ")

# Get coordinates
start_coordinates = get_coordinates(start_place)
end_coordinates = get_coordinates(end_place)

# Directions API
direction_url = "https://api.openrouteservice.org/v2/directions/driving-car"

payload = {
    "coordinates": [
        start_coordinates,
        end_coordinates
    ]
}

headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}

response = requests.post(
    direction_url,
    json=payload,
    headers=headers
)

data = response.json()

# Extract route details
route = data["routes"][0]["summary"]

distance = route["distance"]
duration = route["duration"]

distance_km = distance / 1000
duration_minutes = duration / 60

print("\nRoute Summary")
print("----------------")
print(f"From: {start_place}")
print(f"To: {end_place}")
print(f"Distance: {distance_km:.2f} km")
print(f"Estimated Time: {duration_minutes:.2f} minutes")