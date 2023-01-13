from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
print(driver.title)
driver.execute_script("document.body.style.zoom= '400%'")
time.sleep(2)
driver.execute_script("document.body.style.zoom= '100%'")
time.sleep(2)
driver.close()