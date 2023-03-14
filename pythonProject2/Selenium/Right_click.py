from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH,"//span[text()='right click me']")
act = ActionChains(driver)
act.context_click(button)   # Mouse actions Right Click
act.perform()
time.sleep(4)
driver.find_element(By.XPATH,'//li[@class="context-menu-item context-menu-icon context-menu-icon-copy"]').click()
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()
