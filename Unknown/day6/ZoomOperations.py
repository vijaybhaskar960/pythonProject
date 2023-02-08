from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.execute_script("document.body.style.zoom= '400%'")
time.sleep(3)
driver.execute_script("document.body.style.zoom= '0%'")
time.sleep(3)
driver.close()

