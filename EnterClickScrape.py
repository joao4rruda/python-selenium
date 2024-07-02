import time
from datetime import datetime
from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def hours_to_minutes(hours):
    output = hours.split(" ")[1]
    return output


data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime("%d/%m/%Y")


def main():
    time.sleep(2)
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                  value="/html/body/div[1]/div/h1[2]")

    with open('temperature.txt', 'a') as arquvio:
        arquvio.write(
            str(clean_text(element.text)) + " " + str(data_hora_atual) + '\n')

    return clean_text(element.text)


while True:
    print(main(),
          data_formatada + " " + str(hours_to_minutes(str(data_hora_atual))))
