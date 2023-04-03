import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.python.org/")
driver.find_element(By.XPATH, "//li[@id='downloads']//a[normalize-space()='Downloads']").click()
driver.find_element(By.XPATH, "//div[@class='download-os-windows']//a[@class='button'][normalize-space()='Download Python 3.11.2']").click()
time.sleep(5)

