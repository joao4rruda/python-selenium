import requests

from pprint import pprint

API_key = "de84a73c7b7e4f5c4ceba27920c9ff19"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter a city Name : ")
Final_Url = base_url + "appid=" + API_key + "&q=" + city_name

weather_data = requests.get(Final_Url).json()

print("\nCurrent Weather Data Of" + city_name +":\n")
pprint(weather_data)