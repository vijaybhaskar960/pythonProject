from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.save_screenshot("Myntra.png")

driver.close()