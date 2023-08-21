import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

""" One Method """
element = driver.find_element(By.ID, 'nav-link-accountList')
driver.execute_script("arguments[0].click();", element)

#driver.find_element(By.ID, 'nav-link-accountList').send_keys(Keys.ENTER)
#driver.find_element(By.ID, 'nav-link-accountList').submit()


# Another Method
# element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.ID, "nav-link-accountList")))
# element.click()
time.sleep(4)
driver.close()