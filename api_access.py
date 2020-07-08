# Weather app designed to display the current weather data
# by using the openweathermap api for python

# importing the necessary modules
from config import m_api_key
import requests
from datetime import datetime


# function to convert from kelvin to fahrenheit
def kel_to_fah(kelvin) -> float:
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    # limit decimal point to 2 places after
    fahrenheit = float("{:.2f}".format(fahrenheit))
    return fahrenheit


# function to receive current time in civilian time
def get_current_time() -> str:
    now = datetime.now().strftime("%H:%M")
    current_time_list = now.split(":")
    hour = int(current_time_list[0])
    minutes = current_time_list[1]

    if hour > 12:
        hour -= 12
    current_time = "" + str(hour) + ":" + minutes
    return current_time


# function to find the weather data using openweathermap
def get_weather(m_city, m_state) -> dict:
    # openweathermap api key - if you want to use this app sign up for an OpenWeatherMap
    # free account to get an api key and place it here
    api_key = m_api_key

    # url before adding city name and api key
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="

    # asking for city name
    city = m_city
    state = m_state
    # url after adding city name, state, and api key
    if m_state is not None:
        complete_url = base_url + city + ',' + state + "&appid=" + api_key
    else:
        complete_url = base_url + city + "&appid=" + api_key

    # get the response from openweathermap
    response = requests.get(complete_url)

    # convert the response into json format
    x = response.json()

    # check if a response was recieved
    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        current_temperature = kel_to_fah(current_temperature)

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        current_time = get_current_time()

        data = {"temp": current_temperature, "humidity": current_humidity,
                "description": weather_description, "time": current_time}
        return data

    else:
        print("city is not found")
