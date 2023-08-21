import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
driver.execute_script("alert('Vijay and Vaishu')")
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()
