import requests
import pandas as pd

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = 'c03e8b4cda610415286966adc4aeeead'  
    cities = pd.read_csv('cities.csv')

    for index, row in cities.iterrows():
        city = row['city']
        weather_data = get_weather(city, api_key)
        if weather_data:
            print(f"Weather in {city}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Description: {weather_data['weather'][0]['description']}")
            print("----------")
        else:
            print(f"Could not retrieve weather data for {city}")

if __name__ == "__main__":
    main()
    