from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.zomato.com/india")
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get("https://www.amazon.in/")
driver.switch_to.new_window('tab')
driver.get("https://www.myntra.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.flipkart.com/")


windows = driver.window_handles
print("default title is:",driver.title)

driver.switch_to.window(windows[0])
print("window0 title is:",driver.title)
time.sleep(3)
driver.switch_to.window(windows[1])
print("window1 title is:",driver.title)
time.sleep(3)
driver.switch_to.window(windows[2])
print("window2 title is:",driver.title)
time.sleep(3)
driver.switch_to.window(windows[3])
print("window3 title is:",driver.title)
time.sleep(3)
driver.switch_to.window(windows[0])
print("window0 title is:",driver.title)
time.sleep(3)

driver.quit()