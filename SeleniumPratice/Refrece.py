from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.refresh()
time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()


