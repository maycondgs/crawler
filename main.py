from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as condicao_esperada


def iniciar_driver():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--remote-debugging-pipe')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--headless')


    service = Service()

    driver = webdriver.Chrome(service=service, options=chrome_options)


    wait = WebDriverWait(
        driver,
        50,
        poll_frequency=5,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver,wait


driver, wait = iniciar_driver()

login = '11962802400'
password = 'Salmo91$'


driver.get('https://accounts.latamairlines.com/')
sleep(5)

try:
    btn_cookie = wait.until(condicao_esperada.element_to_be_clickable(By.XPATH, '/html/body/div[1]/div/dialog/div/div/div/div/div/section/div/button[2]'))

    btn_cookie.click()

except:
    pass

sleep(5)


# REDIRECIONA PARA PAGINA DE LOGIN
btn_login = driver.find_element(By.XPATH, '/html/body/div/div/header/div[1]/div[2]/div[2]/button')
driver.execute_script("arguments[0].click();", btn_login)

input_login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/div/input')
input_login.send_keys(login)

btn_next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[3]/div/div/div[1]/button')
btn_next_page.click()

sleep(5)

input_password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/div/div/input')
input_password.send_keys(password)

btn_next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[3]/div/div/div/button')
btn_next_page.click()


btn_login_acess = wait.until(condicao_esperada.element_to_be_clickable(By.XPATH, '/html/body/div/div/header/div[1]/div[2]/div[2]/div/div/button'))

name_login_user = driver.find_element(By.XPATH, '/html/body/div/div/header/div[1]/div[2]/div[2]/div/div/button/span[2]').text

print(name_login_user)

driver.close()