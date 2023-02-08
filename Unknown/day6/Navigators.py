from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.myntra.com/')
driver.maximize_window()
driver.forward()
time.sleep(4)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(4)
driver.close()
