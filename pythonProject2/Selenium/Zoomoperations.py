from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.execute_script("document.body.style.zoom= '300%'")
time.sleep(3)
driver.execute_script("document.body.style.zoom= '0%'")
time.sleep(3)

driver.close()