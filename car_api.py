import requests
import json

url = "https://car-api2.p.rapidapi.com/api/models"

querystring = {"sort":"id","direction":"asc"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "car-api2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

with open('models_api.json', 'w') as outfile:
    json.dump(response.text(), outfile)
