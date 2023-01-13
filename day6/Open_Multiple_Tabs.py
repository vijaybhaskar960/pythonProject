from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj =Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get('https://www.myntra.com/')
driver.switch_to.new_window('tab')
driver.get('https://www.flipkart.com/')
driver.quit()

