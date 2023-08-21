import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
driver.maximize_window()
driver.find_element(By.ID, 'input-firstname').send_keys("Vijay")
driver.find_element(By.ID, 'input-lastname').send_keys("Vaishu")
driver.find_element(By.ID, 'input-email').send_keys("Vijayvaishu@gmail.com")
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).pause(3).send_keys("Vijay")\
    .send_keys(Keys.TAB).pause(3).send_keys("Vaishu").pause(3).send_keys(Keys.TAB)\
    .send_keys("Vijayvaishu@gmail.com").pause(3)\
    .send_keys(Keys.TAB).send_keys('9603449098').send_keys(Keys.TAB).pause(3)\
    .send_keys("9603449098").send_keys(Keys.TAB).pause(3)\
    .send_keys("9603449098").send_keys(Keys.TAB).send_keys(Keys.TAB)\
    .send_keys(Keys.TAB).perform()

time.sleep(5)
driver.close()