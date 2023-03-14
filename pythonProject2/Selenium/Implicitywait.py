from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"nav-link-accountList").click()
driver.find_element(By.NAME,'email').send_keys('8074517920')
driver.find_element(By.ID,"continue").click()
driver.find_element(By.ID,"ap_password").send_keys('vijay@gmail.com')
driver.find_element(By.ID,'signInSubmit').click()

driver.close()

