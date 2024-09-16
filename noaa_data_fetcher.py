import random

def fetch_weather_data(start_lat, start_lon, end_lat, end_lon):
    """
    Simulates fetching weather data for a route between two points.
    In practice, this would be an API call to NOAA or another weather service.
    """
    weather_data = {
        "wind_speed": random.uniform(5, 20),  # Wind speed in knots
        "wave_height": random.uniform(1, 5),  # Wave height in meters
        "storm_warning": random.choice([True, False])  # Random storm warning
    }
    print(f"Fetched weather data: {weather_data}")
    return weather_data

def fetch_ocean_data(start_lat, start_lon, end_lat, end_lon):
    """
    Simulates fetching ocean current data for a route between two points.
    In practice, this would be an API call to NOAA or another ocean data service.
    """
    ocean_data = {
        "current_speed": random.uniform(0.5, 3),  # Current speed in knots
        "current_direction": random.uniform(0, 360)  # Current direction in degrees
    }
    print(f"Fetched ocean data: {ocean_data}")
    return ocean_data
