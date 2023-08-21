import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
# http://username:password@url
# We can pass usernsme and password along with url
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME, 'p').text)
time.sleep(5)
driver.close()