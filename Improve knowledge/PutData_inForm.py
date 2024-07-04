import requests
import pandas as pd
import csv

api_link = "https://newsapi.org/v2/everything?"
api_key = "80423fcb354f45ea8fb17e14b61fc04a"

def get_news(api_link, topic, from_date, sort_by, api_key):
    url = f"{api_link}q={topic}&from={from_date}&sortBy={sort_by}&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        articles = content.get('articles', [])
        return articles
    else:
        print(f"Failed to fetch new. Status code: {response.status_code}")
        return []
    
def write_news_to_csv(articles):
    if not articles:
        print("No articles to write.")
        return
    
    data = [(articles['author'], articles['title'], articles['description'], articles['content'])]

    data_frame = pd.DataFrame(data, columns=['Title', 'Description'])
    data_frame.to_csv('new.csv', index=False, encoding='utf-8')
    print("News written to news.csv")

def main():
    topic = input("Tópico: ")
    from_date = input("A partir da data (formato YYY-MM-DD): ")
    sort_by = "popularity"

    articles = get_news(api_link, topic, from_date, sort_by, api_key)
    write_news_to_csv(articles)

    if __name__ == "__main__":
        main()