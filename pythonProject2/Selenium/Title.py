from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
# Print title of the page
print(driver.title)

# Using the javaScript print the title of the page
title = driver.execute_script("return document.title")
print(title)

driver.close()