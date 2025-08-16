import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import convert_to_fahrenheit, format_timestamp

API_KEY = "YOUR_API_KEY"  # put your OpenWeatherMap API key here
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city: str):
    """Fetch 5-day weather forecast from OpenWeather API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

def process_data(data):
    """Process weather data into DataFrame with converted units."""
    forecast_list = data["list"]
    records = []
    for item in forecast_list:
        timestamp = format_timestamp(item["dt_txt"])
        temp_c = item["main"]["temp"]
        temp_f = convert_to_fahrenheit(temp_c)
        humidity = item["main"]["humidity"]
        wind_speed = item["wind"]["speed"]
        records.append([timestamp, temp_f, humidity, wind_speed])
    
    df = pd.DataFrame(records, columns=["Time", "Temp (°F)", "Humidity (%)", "Wind (m/s)"])
    return df

def plot_weather(df, city):
    """Plot weather trends and save them as PNG files."""
    sns.set(style="darkgrid")

    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Time", y="Temp (°F)", data=df, marker="o")
    plt.xticks(rotation=45)
    plt.title(f"Temperature Forecast for {city}")
    plt.tight_layout()
    plt.savefig("temperature.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Time", y="Humidity (%)", data=df, color="blue", marker="s")
    plt.xticks(rotation=45)
    plt.title(f"Humidity Forecast for {city}")
    plt.tight_layout()
    plt.savefig("humidity.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Time", y="Wind (m/s)", data=df, color="green", marker="^")
    plt.xticks(rotation=45)
    plt.title(f"Wind Speed Forecast for {city}")
    plt.tight_layout()
    plt.savefig("wind.png")
    plt.close()

def main():
    city = input("Type your city name: ")
    data = get_weather_data(city)
    if data:
        df = process_data(data)
        print("\nSample Forecast Data:")
        print(df.head())
        plot_weather(df, city)
        print("\nWeather charts saved: temperature.png, humidity.png, wind.png")

if __name__ == "__main__":
    main()
