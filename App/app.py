import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="WeatherWhiz",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# OpenWeatherMap API key and base URL
API_KEY = "318ae3121b4219f5dc3243d9693c7146"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Uses metric units for temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Streamlit App

st.title("WeatherWhiz - A Weather App")
st.write("WeatherWhiz is a user-friendly web application designed to provide instant weather insights.")
st.header("Enter information below: ")

city = st.text_input("Enter Location: ")
if st.button("Get Weather Information"):
    weather_data = get_weather(city)
    if weather_data["cod"] == 200:
        st.write(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        st.write("Location not found.")

