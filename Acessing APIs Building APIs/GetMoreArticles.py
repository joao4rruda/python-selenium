import requests

api_Key = "80423fcb354f45ea8fb17e14b61fc04a"
api_link = "https://newsapi.org/v2/everything?"
sort_by = "popularity"

topic = input("Tópico: ")
from_date = input("A partir da data: ")

def get_news(topic, from_date , api_Key):
    url = (f'{api_link}'
           f'q={topic}&'
           f'from={from_date}&'
           f'sortBy={sort_by}&'
           f'apiKey={api_Key}')
    response = requests.get(url)
    print(response.json())

get_news(topic, from_date, api_Key)
