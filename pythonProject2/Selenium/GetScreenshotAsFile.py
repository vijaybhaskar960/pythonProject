import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()
driver.get_screenshot_as_file("Selenium.png")
driver.find_element(By.XPATH, "//div[@id='search']//button").click()
driver.get_screenshot_as_file("Search.png")
time.sleep(5)
driver.close()