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

with open('models_api.json', 'w') as outfile:
    json.dump(json_string, outfile, indent=4)

# df = pd.json_normalize(response.json())
# print(df)
 