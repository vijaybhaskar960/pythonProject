from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
Title = driver.title
print("Title is :",Title)
time.sleep(3)
driver.close()