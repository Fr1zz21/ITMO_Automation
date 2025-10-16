from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options=options)

#options.add_argument("--incognito")
#options.add_argument("--headless")
#options.add_argument("--ignore-certificate-errors")
#options.add_argument("--window-size= 1920, 1080")
options.page_load_strategy = 'none'
#options.add_argument("--disable-cache")

driver.get('https://www.saucedemo.com/')
options.page_load_strategy = 'none'


""" url = driver.current_url
print(url)
current_title = driver.title
print(current_title)

assert url == 'https://www.saucedemo.com/',"ERROR, открыта не та страница"

assert current_title == 'Swag Labs', "ERROR, не корректный заголовок"



Username_field  = driver.find_element("xpath", '//input[@id="user-name"]')
Username_field.send_keys('21.igor.com@mail.ru')
print('Логин поля: ', Username_field.get_attribute("value"))

button_main = driver.find_element("xpath", "//input[@type='submit']")
button_main.click() """

time.sleep(5)