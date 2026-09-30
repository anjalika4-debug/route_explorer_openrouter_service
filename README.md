# Route Explorer using OpenRouteService API

## Overview

Route Explorer is a Python application that uses OpenRouteService APIs to find routes between two places.

The application takes place names as input, converts them into coordinates using the Geocoding API, and then uses the Directions API to calculate distance and travel time.

## Features

- Convert place names into coordinates
- Calculate driving routes
- Display distance in kilometers
- Display estimated travel time
- Secure API key handling using environment variables

## Technologies Used

- Python
- OpenRouteService API
- Requests library
- python-dotenv
- JSON

## How It Works

1. User enters starting place and destination.
2. Geocoding API converts place names into coordinates.
3. Directions API calculates the route.
4. Python processes the API response.
5. Application displays route summary.

## Example Output

From: Bengaluru
To: Mysore
Distance: 141.22 km
Estimated Time: 109.26 minutes


## Setup

Install dependencies:


pip install -r requirements.txt


Create a `.env` file:


ORS_API_KEY=your_api_key_here


Run:


python app.py
