import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

for i in range(1,6):
    xpath_txt = "(//div[@id='LinkList1']//a)["+str(i)+"]"
    time.sleep(4)
    driver.find_element(By.XPATH, xpath_txt).click()
    driver.back()

time.sleep(3)
driver.quit()


