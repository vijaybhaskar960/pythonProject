from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.close()
