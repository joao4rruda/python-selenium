from selenium import webdriver
from datetime import datetime as dt
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/account/login? return_url=%2Faccount")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by="ID", value="CustomerEmail").send_keys("app7flask@gmail.com")
    time.sleep(2)
    driver.find_element(by="ID", value="CustomerPassword").send_keys("??!65EhGMg8.WwY" + Keys.RETURN)
    print(driver.current_url)


print(main())