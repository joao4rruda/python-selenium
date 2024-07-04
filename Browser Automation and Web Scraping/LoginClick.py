from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def get_driver():
    #Definir opção para facilitar a navegação
    options = webdriver.ChromeOptions()

    options.add_argument(
        "disable-infobars"
    )  # Isso fará é que, em um navegador, às vezes temos essas barras aqui que exibem algumas informações como se a memória está baixa ou coisas do gênero. essas barras podem interferir no acesso ao script realizando ações do computador

    options.add_argument(
        "start-maxiized")  #Abrir versão maximizada do navegador

    options.add_argument(
        'disable-dev-shm-usage'
    )  #Essa opção específica serve para evitar alguns problemas que ocorrem quando você interage com um navegador em um computador Linux.

    options.add_argument("no-sandbox")

    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )  #Essas opções experimentais são opções que ajudam o selênio a evitar a detecção pelo navegador. Portanto alguns navegadores, páginas da Web, não gostam de scripts. Portanto habilitam nossos scripts para acessar esses navegadores. Portanto, se outro não for de fato isso. é uma opção de adicionar argumento, não é uma opção experimental.

    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.C/hrome(
        options)  #A variável options contém todos os argumentos
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated") #Escreve na tela
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" +
                                                        Keys.RETURN) #Escreve na tela e aperta enter
    time.sleep(2)
    print(driver.current_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print(driver.current_url)

print(main())
