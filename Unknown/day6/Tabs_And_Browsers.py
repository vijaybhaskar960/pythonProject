from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

'''Selenium4 Opens a new tab and switch to new tab'''

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get('https://www.myntra.com/')

'''Selenium4: Opens a new Browser window and switch to new window.'''

driver.switch_to.new_window('window')
driver.get('https://www.python.org/')
driver.quit()


