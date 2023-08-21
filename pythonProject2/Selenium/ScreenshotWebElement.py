import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()
search_button = driver.find_element(By.XPATH, "//div[@id='search']//button")
search_button.screenshot(r"C:\Users\vijay\PycharmProjects\pythonProject3\pythonProject2\Selenium\Screenshot\search.png")
time.sleep(3)
driver.quit()