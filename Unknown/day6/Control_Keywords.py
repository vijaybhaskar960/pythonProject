from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://text-compare.com/')
driver.maximize_window()
input = driver.find_element(By.ID,'inputText1')
input2 = driver.find_element(By.ID,'inputText2')
input.send_keys("Welcome to the new world")

act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys('a')
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL)
act.send_keys('c')
act.key_up(Keys.CONTROL)
act.perform()

act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL)
act.send_keys('v')
act.key_up(Keys.CONTROL)
act.perform()
driver.close()

