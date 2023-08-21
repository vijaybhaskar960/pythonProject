from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[value='Performance']").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[value='Automation']").click()
time.sleep(3)
driver.close()

