from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.myntra.com/')
driver.maximize_window()
driver.execute_script("window.scroll(0,500)")
time.sleep(4)
# Approach 2 scroll down page till end
driver.execute_script("window.scroll(0,document.body.scrollHeight)")
time.sleep(4)
value = driver.execute_script('return window.pageYOffset;')
print('How many pixels moved is:',value)

print(driver.title)
# Approach 2 scroll up page till end
driver.execute_script('window.scroll(0,-document.body.scrollHeight)')
time.sleep(3)
driver.close()
