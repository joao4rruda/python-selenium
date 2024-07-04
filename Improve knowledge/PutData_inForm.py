import requests
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 

import time

# region GET DRIVER

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

# region MAIN
def main():

    topic = input("Tópico: ")
    from_date = input("A partir da data (formato YYY-MM-DD): ")
    sort_by = "popularity"

    articles = get_news(api_link, topic, from_date, sort_by, api_key)
    organize_data_to_write(articles)

# region GET NEWS

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
    
def organize_data_to_write(articles):
    if not articles:
        print("No articles to write.")
        return
    
    data = [(article['author'], 
             article['title'], 
             article['description'], 
             article['content'],
             article['url'],
             article['urlToImage'],
             article['publishedAt']) for article in articles]
    

    for author, title, description, content, url, urlToImage, publishedAt, in data:
        put_in_form(author , title, description, url, content, urlToImage, publishedAt)

# region AUTOMATION FORM
def put_in_form(author, title, description, content, url, urlToImage, publishedAt):
    if author != "[Removed]" and title != "[Removed]" and content != "[Removed]":

        driver = get_driver()
        driver.maximize_window()

        # Author
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(author) 
        
        # Title
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(title)
        
        # Description
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(description)
        
        # Content
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(content)
        
        # URL 
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(url)
        
        # url da imagem
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(urlToImage)
        
        # publicado em
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(publishedAt)
        

        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

main()