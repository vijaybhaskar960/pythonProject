from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.myntra.com/')
driver.maximize_window()
driver.save_screenshot(r'C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\day6\myntra_screenshot.png')
driver.close()