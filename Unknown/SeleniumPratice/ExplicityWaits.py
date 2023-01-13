# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

# get element after explicitly waiting for 10 seconds
element = WebDriverWait(driver, 10)
element.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/ul[1]/li[1]/span")))
print(driver.title)
# click the element
driver.close()



