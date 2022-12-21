from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()

driver.execute_script('window.open("https://www.myntra.com/")')
time.sleep(3)
driver.execute_script('window.open("https://www.amazon.in/")')
time.sleep(2)
driver.quit()