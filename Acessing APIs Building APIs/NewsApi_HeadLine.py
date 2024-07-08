import requests

def get_weather(city, units='metrics', api_key=''):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={city}&appid={api_key} & units={units}"
    r = requests.get(url)
    content = r.json()
    return content

print(get_weather(city='Washington'))