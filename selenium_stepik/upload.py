from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import os
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options=options)
from selenium.webdriver.common.by import By


driver.get('https://demoqa.com/upload-download')

upload_filed = driver.find_element(By.XPATH,'//div/input[@type="file"]')
upload_filed.send_keys(f"{os.getcwd()}/downloads/testDragDrop.txt")