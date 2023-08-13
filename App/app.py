import streamlit as st
import requests

# OpenWeatherMap API key and base URL
API_KEY = ""
BASE_URL = ""

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Uses metric units for temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data