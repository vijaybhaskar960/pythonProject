from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Open chrome browswer
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple')
d.maximize_window()
d.switch_to.frame("iframeResult")
# d.find_element(By.ID,"iframeResult")
cars = d.find_element(By.XPATH,'//*[@id="cars"]')
Dropdown = Select(cars)
Dropdown.select_by_value("saab")
Dropdown.select_by_value("audi")
time.sleep(3)
d.close()
