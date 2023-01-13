from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/radio.html")
driver.find_element(By.ID,"vfb-7-2").click()
time.sleep(2)
driver.close()
