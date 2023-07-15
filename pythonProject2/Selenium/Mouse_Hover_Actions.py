from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)


driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(3)
more = driver.find_element(By.XPATH,"//span[@class='more-arr']")
my_account = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
actions = ActionChains(driver)
actions.move_to_element(my_account).perform()
actions.move_to_element(more).perform()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
time.sleep(3)
driver.close()
