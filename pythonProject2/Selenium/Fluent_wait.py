
from selenium.common import NoSuchElementException
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
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList"))).click()
time.sleep(3)
driver.close()
