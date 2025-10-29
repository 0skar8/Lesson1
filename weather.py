from dotenv import load_dotenv
from os import getenv
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    response = requests.get(request_url)
    return response.json()

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions *** \n\n")
    
    city = input("\n Please enter a city name: \n")
    
    weather_data = get_current_weather(city)
    
    print("\n")
    print(weather_data)