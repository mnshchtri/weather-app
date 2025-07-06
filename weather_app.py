import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise Exception("Missing OpenWeatherMap API key. Please set the OPENWEATHER_API_KEY environment variable.")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    
    if response.status_code != 200:
        error_message = weather_data.get('message', 'Unknown error occurred')
        raise Exception(f"API request failed: {error_message}")
    
    if 'main' not in weather_data or 'temp' not in weather_data['main']:
        raise Exception("Unexpected data structure in API response")
    
    temp_kelvin = weather_data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    return round(temp_celsius, 2)

def main():
    city = input("Enter the city name: ")
    try:
        temperature = get_weather(city)
        print(f"Current temperature in {city} is {temperature}°C")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

