from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome()
d.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
d.maximize_window()
d.switch_to.frame("packageListFrame")
time.sleep(4)
d.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(4)
d.switch_to.default_content()
time.sleep(2)
d.switch_to.frame("packageFrame")
time.sleep(2)
d.find_element(By.CLASS_NAME,"interfaceName").click()
d.switch_to.default_content()
time.sleep(5)
d.switch_to.frame("classFrame")
time.sleep(4)
d.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
time.sleep(4)
d.close()

