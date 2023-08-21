import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resizable/#content")
driver.maximize_window()

ele = driver.find_element(By.XPATH, '//div[@class="demo-list"]')
ele.screenshot(r"C:\Users\vijay\PycharmProjects\pythonProject3\pythonProject2\Selenium\Screenshot\Particular.png")
time.sleep(3)
driver.quit()
