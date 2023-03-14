from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()
element = driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")

drp = Select(element)
drp.select_by_value('BEL')
drp.select_by_visible_text('Canada')
drp.select_by_index(2)

driver.close()