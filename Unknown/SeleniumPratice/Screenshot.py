from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.save_screenshot(r"C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\SeleniumPratice\selenium.png")
time.sleep(5)
driver.close()