import requests

api_Key = "80423fcb354f45ea8fb17e14b61fc04a"
topic = input("Tópico: ")
from_date = input("A partir da data: ")

def get_news(topic, from_date , api_Key):
    url = (f'https://newsapi.org/v2/everything?'
           f'q={topic}&'
           f'from={from_date}&'
           f'sortBy=popularity&'
           f'apiKey={api_Key}')
    response = requests.get(url)
    print(response.json())

get_news(topic, from_date, api_Key)
