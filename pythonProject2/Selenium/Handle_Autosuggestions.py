import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element(By.ID, 'fromCity').click()
driver.find_element(By.XPATH, '//input[@placeholder="From"]').send_keys('b')

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.close()