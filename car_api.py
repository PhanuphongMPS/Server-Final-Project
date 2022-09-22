import requests
import json
import pandas as pd

url = "https://smartcar.p.rapidapi.com/vehicles"

headers = {
	"Authorization": "<REQUIRED>",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "smartcar.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

with open('models_api.json', 'w') as outfile:
    json.dump(response.json(), outfile, indent=4)

df = pd.json_normalize(response.json())
print(df)
 