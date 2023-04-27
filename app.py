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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)