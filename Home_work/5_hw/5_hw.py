import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
def search_elements():
    driver.get('https://www.saucedemo.com/')
    url = driver.current_url
    current_title=driver.title
    if url == 'https://www.saucedemo.com/':
        print(url, current_title)
    else:
        print('ERROR')
    Login=driver.find_element('xpath','//input[@id ="user-name"]')
    Password=driver.find_element('xpath','//input[@id ="password"]')
    Submit_Botton=driver.find_element('xpath','//input[@type ="submit"]')
    if Login and Password and Submit_Botton:
        print('Элементы найдены')
    else:
        print('Ошибка')
search_elements()


time.sleep(5)