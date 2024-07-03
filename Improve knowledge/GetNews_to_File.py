import requests

api_link = "https://newsapi.org/v2/everything?"

topic = input("Tópico: ")
from_date = input("A partir da data: ")

sort_by = "popularity"
api_Key = "80423fcb354f45ea8fb17e14b61fc04a"


def get_news(api_link, topic, from_date , sort_by, api_Key):
    url = (f'{api_link}'
           f'q={topic}&'
           f'from={from_date}&'
           f'sortBy={sort_by}&'
           f'apiKey={api_Key}')
    response = requests.get(url)
    print(response.json())

def write_news(){
    
}

def main():
    get_news(api_link, topic, from_date , sort_by, api_Key)

main()