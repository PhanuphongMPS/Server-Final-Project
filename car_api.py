import requests
import json
import pandas as pd

url = "https://car-api2.p.rapidapi.com/api/models"

querystring = {"sort":"id","direction":"asc"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "car-api2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# df = pd.json_normalize(response.json())
# print(df)
 