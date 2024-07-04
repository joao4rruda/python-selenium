import requests
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# region request API

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
    
    data = [(article['author'], article['title'], article['description'], article['content']) for article in articles]
    
    for author, title, description, content in data:
        put_in_form(author, title, description, content)

    # data_frame = pd.DataFrame(data, columns=['Title', 'Description'])
    # data_frame.to_csv('new.csv', index=False, encoding='utf-8')
    # print("News written to news.csv")


# region processo de automação

def put_in_form(author, title, description, content):

        driver = get_driver()
        # Author
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(author)
        time.sleep(4)

        # Title
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(title)
        time.sleep(4)

        # Description
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(description)
        time.sleep(4)

        # Content
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(content)
        time.sleep(4)


def get_driver():
    options = webdriver.ChromeOptions()

    options.add_argument('disable-infobars')
    options.add_argument('start-maxiized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')

    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )

    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(
        options
    )

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScswuDL2q7FS1OI2Cru3NY1X9kpBZiFN9F7f8t45JlXB712yA/viewform")
    return driver

def main():

    topic = input("Tópico: ")
    from_date = input("A partir da data (formato YYY-MM-DD): ")
    sort_by = "popularity"

    articles = get_news(api_link, topic, from_date, sort_by, api_key)
    write_news_to_csv(articles)

    driver = get_driver()

    if __name__ == "__main__":
        main()


main()
