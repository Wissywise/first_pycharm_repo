import requests
from bs4 import BeautifulSoup

api_key = "ce0a8d604a8d94b38109ce7ec9e2cdc9"

city = "London" # You can change this to any city you want to get the weather data for

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

params = {
    "q": city, # City name
    "appid": api_key, # Your OpenWeatherMap API key
    "units": "metric"} # Celsius

response = requests.get(url, params=params) # Send a GET request to the OpenWeatherMap API with the specified parameters

if response.status_code == 200:
    data = response.json() # Parse the JSON response
    """print(f"Weather data for {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")"""
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    print(f"Weather data in {city}: Weather: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

#soup = BeautifulSoup(response.text, 'html.parser') # Parse the JSON response using BeautifulSoup

