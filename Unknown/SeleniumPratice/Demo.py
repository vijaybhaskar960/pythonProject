from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("8074517920")
driver.find_element(By.XPATH,'//input[@id="continue" and @class="a-button-input"]').click()
driver.find_element(By.NAME ,"password").send_keys("Vijayreddy")

driver.find_element(By.ID,"signInSubmit").click()
time.sleep(5)

driver.close()