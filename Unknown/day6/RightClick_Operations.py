import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
Dou_Click = driver.find_element(By.XPATH,"//span[text()='right click me']")
act = ActionChains(driver)
act.context_click(Dou_Click).perform()

driver.find_element(By.XPATH,'//li[@class="context-menu-item context-menu-icon context-menu-icon-delete"]').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(4)
driver.close()

