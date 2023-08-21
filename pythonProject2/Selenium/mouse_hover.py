import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu/")
driver.maximize_window()
ele = driver.find_element(By.XPATH, "//a[text() = 'Main Item 2']")
actions = ActionChains(driver)
#actions.move_to_element(ele).perform()
time.sleep(5)
sub = driver.find_element(By.XPATH, "//a[text() = 'SUB SUB LIST »']")
#actions.move_to_element(sub).perform()
time.sleep(5)
txt = driver.find_element(By.XPATH, "//a[text() = 'Sub Sub Item 1']")
#actions.move_to_element(txt).perform()


actions.move_to_element(ele).move_to_element(sub).move_to_element(txt).perform()
time.sleep(10)