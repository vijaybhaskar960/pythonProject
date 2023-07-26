import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
#options.add_argument('--incognito')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get('https://www.yatra.com/')
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get("https://www.amazon.in/")
time.sleep(5)
driver.switch_to.new_window('tab')
driver.get("https://www.flipkart.com/")
time.sleep(5)

windows = driver.window_handles

driver.switch_to.window(windows[0])
print(driver.title)
time.sleep(5)
driver.switch_to.window(windows[1])
print(driver.title)
time.sleep(3)
driver.switch_to.window(windows[2])
print(driver.title)
driver.quit()


