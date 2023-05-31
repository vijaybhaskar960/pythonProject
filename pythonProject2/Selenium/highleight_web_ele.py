from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()


def high_light_elements(element):
    #driver.execute_script("arguments[0].style.border= '3px solid red'", element)
    #driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid red; background:yellow'", element)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "background:yellow; color:red;border: 5px solid red ")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
high_light_elements(search_box)

time.sleep(5)
driver.close()
