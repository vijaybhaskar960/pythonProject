import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
driver.find_element(By.ID, 'alert1').click()

wait = WebDriverWait(driver, 5)
wait.until(ec.alert_is_present())

Alert = driver.switch_to.alert
alert_txt = Alert.text
print(alert_txt)
time.sleep(3)
Alert.accept()
time.sleep(3)
driver.close()
