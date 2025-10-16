

import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}

options.add_experimental_option('prefs', prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options=options)



driver.get('https://the-internet.herokuapp.com/download')

driver.find_elements(By.XPATH,"//a")[2].click()


time.sleep(3)