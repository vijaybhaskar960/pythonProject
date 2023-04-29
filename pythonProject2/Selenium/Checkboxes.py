from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[value='Performance']").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[value='Automation']").click()
time.sleep(3)
# driver.close()
