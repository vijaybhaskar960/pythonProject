import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.set_window_size(1000,800)
time.sleep(5)
driver.close()