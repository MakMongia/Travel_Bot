import requests

def get_weather(city):
    """
    Fetches the current weather data for a specified city using the OpenWeatherMap API.

    Parameters:
    city (str): The name of the city for which to retrieve the weather data.

    Returns:
    dict: A dictionary containing the weather data if the request is successful.
    None: If the request fails (e.g., invalid city name or API request limit exceeded).
    """
    api_key = 'INSERT YOUR API KEY'  # Your OpenWeatherMap API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'  # Base URL for the OpenWeatherMap API

    # Parameters for the API request
    params = {
        'q': city,  # City name
        'appid': api_key,  # API key
        'units': 'metric'  # Units of measurement (metric for Celsius)
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()
        return data
    else:
        # Return None if the request failed
        return None
