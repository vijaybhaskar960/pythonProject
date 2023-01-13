from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
print(driver.page_source)
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.switch_to.new_window("tab")
driver.get()
driver.refresh()
time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()


