import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
links = driver.find_element(By.TAG_NAME, "a")
print("number of links", links)
Alert(driver).authenticate("username", "password")

time.sleep(5)
driver.close()