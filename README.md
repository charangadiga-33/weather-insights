# Python Weather Insights

This is a simple Python project to check and visualize the 5-day weather forecast for any city.  
It uses the OpenWeatherMap API to get weather data and shows it with pandas, matplotlib, and seaborn.

---

## Features
- Get 5-day weather forecast using OpenWeatherMap API  
- Shows temperature (in Fahrenheit), humidity, and wind speed  
- Creates simple charts for better understanding  
- Saves the charts as image files (PNG)

---

## Project Structure
py-weather-insights/
│── src/
│ ├── weather_insights.py # main program
│ └── utils.py # helper functions
│── README.md
│── requirements.txt


---


## How to Run
1. Clone the repository:
   git clone https://github.com/your-username/py-weather-insights.git
  cd py-weather-insights/src
  
2. Install the requirements:
   pip install -r ../requirements.txt

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

4. Add your API key in the code:
```python
API_KEY = "YOUR_API_KEY"
```
5. Run the program:
   python weather_insights.py
