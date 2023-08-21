import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.amazon.in/")
print(driver.title)
links = driver.find_elements(By.TAG_NAME, 'a')
print("Links in Amazon Home Page:", len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT, 'Mobiles').click()
time.sleep(5)
driver.close()