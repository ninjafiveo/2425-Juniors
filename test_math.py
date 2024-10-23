import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "ewok_weather_app")

def get_lat_lon(city, state):
    location = geolocator.geocode(f"{city}, {state}")
    if location:
        return location.latitude, location.longitude
    else:
        return None
    
def test_get_lat_lon():
    city = input("Enter the Earth city name where you'd like to land: ")
    state = input("Enter the state abbreviation (e.g., OH for Ohio): ")
    lat_lon = get_lat_lon(city, state)

    if isinstance(lat_lon, tuple):
        print(f"The latitude and longitude of {city}, {state} are {lat_lon[0]}, {lat_lon[1]}.")
    else:
        print("Location not found.")
test_get_lat_lon()

def get_weather_data(lat, lon):
    base_url = f"https://api.weather.gov/points/{lat},{lon}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        forecast_url = data["properties"]["forecast"]
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        return forecast_response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching weather data: {err}")
        return None

ewok_weather = {}

def update_weather_data(city, state, lat, lon, ewok_weather):
    weather_data = get_weather_data(lat, lon)
    if weather_data:
        ewok_weather[city] = {
            "state": state,
            "current_temperature": weather_data["properties"]["periods"][0]["temperature"],
            "high_temperature": weather_data["properties"]["periods"][1]["temperature"],
            "low_temperature": weather_data["properties"]["periods"][2]["temperature"],
            "weather_conditions": weather_data["properties"]["periods"][3]["detailedForecast"]
        }
        print(f"Weather data for {city}, {state} updated successfully.")
    else:
        print(f"Unable to update weather data for {city}, {state}.")

def display_weather_data(city, ewok_weather):
    weather = ewok_weather.get(city)
    if weather:
        print(f"\nCity: {city}, {weather['state']}")
        print(f"Current Temperature: {weather['current_temperature']}°F")
        print(f"High Temperature: {weather['high_temperature']}°F")
        print(f"Low Temperature: {weather['low_temperature']}°F")
        print(f"Conditions: {weather['weather_conditions']}\n")
    else:
        print(f"No weather data available for {city}.")

while True:
    city = input("Enter the Earth city name where you'd like to land: ")
    state = input("Enter the state abbreviation (e.g., OH for Ohio): ")
    lat_lon = get_lat_lon(city, state)

    if lat_lon:
        update_weather_data(city, state, lat_lon[0], lat_lon[1], ewok_weather)
        display_weather_data(city, ewok_weather)

    else:
        print("Location not found. Please try again.")

    repeat = input("Would you like to check another location? (yes/no): ").lower()

    if repeat != "yes":
        print("Goodbye! Stay safe out there.")
        break