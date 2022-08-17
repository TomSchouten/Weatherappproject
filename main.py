import streamlit as st
import requests


st.title("Weather App") # Displays title
st.subheader("Exploring RapidAPI's weather Endpoints") # Displays subheader

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
	"X-RapidAPI-Key": "5a38b24a20msh5e55cfbff1e7e03p1b44b7jsn91f56f7e209d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
  }

location = st.text_input("Enter the location", "Chennai")
querystring = {"q":{location}}

response = requests.request("GET", url, headers=headers, params=querystring)
result = response.text