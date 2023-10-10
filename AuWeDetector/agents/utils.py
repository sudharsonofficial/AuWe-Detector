import requests

from AuWeDetector.agents.config import WEATHER_API_KEY


def fetch_temperature(city: str) -> float | None:
    """
    Fetches the temperature for a given city using a weather API.

    Args:
        city (str): The name of the city for which the temperature is to be fetched.

    Returns:
        float | None: The temperature in Celsius if successfully fetched, None otherwise.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Coverting Kelvin to Celsius
        temp = round(data['main']['temp'] - 273.15, 3)
        
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp}°C')
        print(f'Description: {desc}')
        return temp
    else:
        print('Error fetching weather data')
        return None
