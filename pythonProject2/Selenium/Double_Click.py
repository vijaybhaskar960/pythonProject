from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//button[text()='Copy Text']")

act = ActionChains(driver)
act.double_click(element).perform()
time.sleep(5)
driver.close()