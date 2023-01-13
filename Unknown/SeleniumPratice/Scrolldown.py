from selenium import webdriver
import time

from selenium.webdriver.common.by import By
def screenshot():
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    driver.execute_script("window.scroll(0,2000)")
    time.sleep(5)
    driver.execute_script("window.scroll(2000,0)")
    # Scrolldown to the page till end
    driver.execute_script("window.scroll(0,document.body.scrollHeight)")
    time.sleep(5)
    driver.close()
screenshot()