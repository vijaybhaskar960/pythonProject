import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.ID, 'nav-link-accountList').click()
driver.find_element(By.ID, 'ap_email').send_keys("8074517920")
time.sleep(3)
driver.find_element(By.ID, 'continue').click()
time.sleep(3)
driver.find_element(By.ID, 'ap_password').send_keys("Vijay123")
time.sleep(3)
# driver.find_element(By.ID, 'signInSubmit').send_keys(Keys.ENTER)
# time.sleep(3)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()
time.sleep(3)