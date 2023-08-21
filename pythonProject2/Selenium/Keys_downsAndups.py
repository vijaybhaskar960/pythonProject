import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
links = driver.find_elements(By.XPATH, '//div[@id="LinkList1"]//a')
for link in links:
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.quit()
