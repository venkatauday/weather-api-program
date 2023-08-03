import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def fetch_weather_data(city):
    url = f"{API_BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_temperature(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['temp']
    return None

def get_wind_speed(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['wind']['speed']
    return None

def get_pressure(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['pressure']
    return None

def print_weather_data(city, date):
    weather_data = fetch_weather_data(city)
    temperature = get_temperature(weather_data, date)
    wind_speed = get_wind_speed(weather_data, date)
    pressure = get_pressure(weather_data, date)

    print(f"\nWeather data for {city} on {date}:")
    if temperature:
        print(f"Temperature: {temperature}°C")
    else:
        print("Temperature data not available.")

    if wind_speed:
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print("Wind speed data not available.")

    if pressure:
        print(f"Pressure: {pressure} hPa")
    else:
        print("Pressure data not available.")

if __name__ == "__main__":
    cities_list = ["London"]
    dates_list = ["2023-08-03", "2023-08-04", "2023-08-05"]

    for city in cities_list:
        for date in dates_list:
            print_weather_data(city, date)
