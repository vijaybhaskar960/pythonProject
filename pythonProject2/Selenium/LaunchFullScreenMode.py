import time
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/")
#driver.fullscreen_window()
time.sleep(5)
driver.close()