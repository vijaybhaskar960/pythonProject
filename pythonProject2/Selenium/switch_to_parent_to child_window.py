from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(5)
print(driver.current_window_handle)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(3)
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

# driver.switch_to.default_content()
# print(driver.title)

driver.switch_to.parent_frame()
print(driver.title)
time.sleep(5)

# Switch to parent window
parent_window_handle = driver.window_handles[0]
driver.switch_to.window(parent_window_handle)
print(driver.title)
time.sleep(5)

# Switch to Child window
child_window_handle = driver.window_handles[-1]
driver.switch_to.window(child_window_handle)
print(driver.title)
time.sleep(5)
driver.quit()


