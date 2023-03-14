from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By



service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame("frame-one1434677811")
time.sleep(3)
driver.find_element(By.ID,'RESULT_FileUpload-10').send_keys("C:/Users/vijay/OneDrive/Documents/output.xml")
time.sleep(5)

driver.close()