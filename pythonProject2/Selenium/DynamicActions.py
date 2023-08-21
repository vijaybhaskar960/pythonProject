import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@id='start']/button").click()
time.sleep(3)

wait = WebDriverWait(driver, 30)
page_wait = wait.until(ec.invisibility_of_element_located((By.ID, 'loading')))
print(driver.find_element(By.XPATH, "//div[@id='finish']/h4").text)
time.sleep(3)
driver.close()