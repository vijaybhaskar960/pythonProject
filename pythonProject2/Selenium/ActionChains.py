import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# element = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
#
# act = ActionChains(driver)
# act.double_click(element)
# act.perform()
# time.sleep(3)
# driver.close()

# driver.find_element(By.XPATH, "//button[text()='Alert']").click()
#driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
# driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("VijayVaishu")
time.sleep(4)
#driver.switch_to.alert.accept()

Alert(driver).accept()
#driver.switch_to.alert.dismiss()
time.sleep(3)

driver.close()

