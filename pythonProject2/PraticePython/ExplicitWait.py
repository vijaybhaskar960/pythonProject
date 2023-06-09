import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
mywait = WebDriverWait(driver,10)
Sigin = mywait.until(EC.element_to_be_clickable((By.ID,"nav-link-accountList")))
Sigin.click()
driver.close()
