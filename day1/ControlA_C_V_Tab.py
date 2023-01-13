# Ctrl+A
# Ctrl+C
# Ctrl+V
# Tab

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
d = webdriver.Chrome()
d.get("https://text-compare.com/")
# d.implicitly_wait(10)
d.maximize_window()
input = d.find_element(By.XPATH,"//textarea[@id='inputText1']")
input1 = d.find_element(By.ID,'inputText2')
input.send_keys("Welcome to New world")
sleep(5)
act=ActionChains(d)
# Ctrl+A
act.key_down(Keys.CONTROL)
act.send_keys('a')
act.key_up(Keys.CONTROL)
act.perform()
d.close()