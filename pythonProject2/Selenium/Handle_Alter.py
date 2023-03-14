from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//a[text() = "Alert with OK & Cancel "]').click()

driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
# driver.switch_to.alert.accept()
time.sleep(4)
driver.switch_to.alert.dismiss()
time.sleep(4)
driver.close()
