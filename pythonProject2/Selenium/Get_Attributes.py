from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.amazon.in/')
driver.maximize_window()
ele = driver.find_element(By.ID,'nav-link-accountList').get_attribute('class')
print(ele)
driver.close()

