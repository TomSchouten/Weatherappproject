import requests
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import seaborn
# delete unused imports at the end

url = "https://weatherapi-com.p.rapidapi.com/history.json"

user_input = 'noordwijk' #input("Enter city: ")
date = date.today()      # Change this param to input if you want to select a specific date. for now it takes the current date

querystring = {"q": user_input,"dt":date,"lang":"en"}

headers = {
	"X-RapidAPI-Key": "5a38b24a20msh5e55cfbff1e7e03p1b44b7jsn91f56f7e209d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

hist_data = requests.request("GET", url, headers=headers, params=querystring)

print(hist_data.text)
print(hist_data.json()['forecast']['forecastday'][0]['hour'][0]['temp_c'])
print(hist_data.json()['forecast']['forecastday'][0]['hour'][0]["time"])

## test voor een array te krijgen met alle temperaturen per uur op de dag



## test voor een array te rijgen met alle bijbehorende uren bij bovenstaande temperaturen



#def GetTemp():
    #temperatures = hist_data['hour'][0]['avgtemp_c']
    #times = hist_data['hour'][0]['time']
    #return temperatures, times

