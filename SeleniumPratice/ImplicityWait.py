from selenium import webdriver

import time

from selenium.webdriver.common.by import By

d = webdriver.Chrome()

d.get("https://www.flipkart.com/")
d.maximize_window()
d.implicitly_wait(10)
d.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
time.sleep(5)
d.close()