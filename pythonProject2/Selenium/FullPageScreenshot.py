import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()

width = 1366
height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

driver.set_window_size(width, height)
page_body = driver.find_element(By.TAG_NAME, "body")
page_body.screenshot(r"C:\Users\vijay\PycharmProjects\pythonProject3\pythonProject2\Selenium\Screenshot\Full_Page_Screenshot.png")
time.sleep(3)

driver.quit()