from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,'//span[@class = "ui-slider-handle ui-corner-all ui-state-default"][1]')

max_slider = driver.find_element(By.XPATH,'//span[@class = "ui-slider-handle ui-corner-all ui-state-default"][2]')

print(min_slider.location)
print(max_slider.location)


act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,200,0).perform()
act.drag_and_drop_by_offset(max_slider,-80,0).perform()

driver.close()

