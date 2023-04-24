from flask import Flask
from weatherwhiz import showWeather

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to WeatherWhiz!'

@app.route('/weather/<city>')
def weather(city):
    weather_info = showWeather(city)
    return weather_info
