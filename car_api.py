import requests
import json
import pandas as pd

url = "https://car-data.p.rapidapi.com/cars"

querystring = {"limit":"10","page":"0"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

with open('models_api.json', 'w') as outfile:
    json.dump(response.json(), outfile, indent=4)

df = pd.json_normalize(response.json())
print(df)
 