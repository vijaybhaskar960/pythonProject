import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)
options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(10)