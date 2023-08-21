import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
driver.maximize_window()
driver.find_element(By.ID, 'newWindowBtn').click()
parentwindow = driver.current_window_handle
print("Parent Window Handles is:", parentwindow)
windows = driver.window_handles
for window in windows:
    print(window)
    if parentwindow != window:
        driver.switch_to.window(window)
        driver.find_element(By.ID, 'firstName').send_keys("VijayaReddy")
        driver.close()
        time.sleep(5)

driver.switch_to.window(parentwindow)
driver.find_element(By.ID,'name').send_keys("Nikitha")
time.sleep(5)
driver.quit()