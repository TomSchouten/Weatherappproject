import requests
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import seaborn
# delete unused imports at the end

url = "https://weatherapi-com.p.rapidapi.com/history.json"

user_input = input("Enter city: ")
date = date.today()
querystring = {"q": user_input,"dt":date,"lang":"en"}

headers = {
	"X-RapidAPI-Key": "5a38b24a20msh5e55cfbff1e7e03p1b44b7jsn91f56f7e209d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

hist_data = requests.request("GET", url, headers=headers, params=querystring)

print(hist_data.text)