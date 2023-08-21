import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source = driver.find_element(By.ID, 'box1')
target = driver.find_element(By.ID, 'box101')
actions = ActionChains(driver)
actions.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)
driver.close()


