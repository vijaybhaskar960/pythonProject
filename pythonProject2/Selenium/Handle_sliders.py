from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty&q=Price%3A85%2C585%7C")
driver.maximize_window()
ele1 = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")

ele2 = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")

ActionChains(driver).drag_and_drop_by_offset(ele1,10,0).perform()
time.sleep(3)
#ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(80,0).release().perform()
#ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(50,0).release().perform()
ActionChains(driver).drag_and_drop_by_offset(ele2,-50,0).perform()

time.sleep(4)
driver.close()