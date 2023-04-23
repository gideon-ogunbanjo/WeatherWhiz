# importing the necessary libraries
from tkinter import *
import requests
import json
from datetime import datetime

# initializing the window

root =Tk()
root.geometry("400x400") # size of the window by default
root.resizable(0,0) # making the window size fixed

#title of the window

root.title("Weather App - Gideon Ogunbanjo") 

city_value = StringVar()
 
def showWeather():
 
# entering the api key, copies from the OpenWeatherMap dashboard
    api_key = "34a2c3b4a0568b76a15230c66d6ba5f0"  #sample API key
 
    # get city name from user from the input field
    city_name = city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # getting the response from the fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   # clearing the text field for every new output
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
 
 
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
#----------- storing the fetched values of weather of a Country
 
        temp = int(weather_info['main']['temp'] - kelvin)                                     # converting the default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
# assigning Values to our weather varaible, to display as an output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nEstimated degree in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time}, and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid Country Name !!"
 
    tfield.insert(INSERT, weather)   # used to insert or send value in our Text Field to display output


# adding functionalities to change the time format, this function checks for the local time as compared to the UTC(Universal Time Coordinated) in which the API gives the output to the time format as per our location. Ex. UTC to IST.    
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


# creating the GUI

city_head= Label(root, text = 'Enter Country/City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack() #entry field

# weather button which we click to check the weather of the user inputted city
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
#Gideon Ogunbanjo