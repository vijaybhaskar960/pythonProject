import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resizable/#content")
driver.maximize_window()
frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(frame)
actions = ActionChains(driver)
dd = driver.find_element(By.XPATH, "//*[@id='resizable']/div[3]")
actions.drag_and_drop_by_offset(dd, 50, 80).perform()
time.sleep(5)
driver.close()

