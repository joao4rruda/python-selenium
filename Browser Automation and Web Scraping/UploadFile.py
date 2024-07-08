import os 

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver


def test_uploads(driver):
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/upload")
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))
    
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    driver.find_element(By.ID, "file-submit").click()
