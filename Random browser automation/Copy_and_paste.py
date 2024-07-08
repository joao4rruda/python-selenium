import sys

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

def get_driver():
    options = webdriver.ChromeOptions()
    

def test_key_down(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver).key_down(Keys.SHIFT).send_keys("abc").perform()
    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "ABC"
