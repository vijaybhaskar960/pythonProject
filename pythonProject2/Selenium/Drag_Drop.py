from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element(By.ID,"box6")
target = driver.find_element(By.ID,'box106')

act = ActionChains(driver)
act.drag_and_drop(source,target)
act.perform()

driver.close()