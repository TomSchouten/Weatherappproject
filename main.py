import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import seaborn
# delete unused imports at the end

url = "https://weatherapi-com.p.rapidapi.com/current.json"

user_input = input("Enter city: ")
querystring = {"q": user_input}

headers = {
	"X-RapidAPI-Key": "5a38b24a20msh5e55cfbff1e7e03p1b44b7jsn91f56f7e209d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

weather_data = requests.request("GET", url, headers=headers, params=querystring)

weather = weather_data.json()['current']['condition']['text']
weather_icon = weather_data.json()['current']['condition']['icon']
temp_c = weather_data.json()['current']['temp_c']
feel_temp = weather_data.json()['current']['feelslike_c']


print(f"The current weather is: {weather}")
print(f"The current temperature is: {temp_c}")
print(f"The current temperature feels like: {feel_temp}")

