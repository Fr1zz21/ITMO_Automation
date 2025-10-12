from selenium.webdriver.common.by import By
from pages.swag_labs import SwagLabs
import time



def found_icon(browser):
    browser.get('https://www.saucedemo.com/')
    time.sleep(10)
    icon = browser.find_element(By.CSS_SELECTOR, 'div.login_logo')
    if icon is None:
        print('Не найден')
    else:
        print('Найден')
    
    #sauce_demo_page = SwagLabs(browser)
    #sauce_demo_page.visit()
    #assert sauce_demo_page.exist_icon()
