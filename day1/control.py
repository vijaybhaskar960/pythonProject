# Ctrl+A
# Ctrl+C
# Ctrl+V
# Tab
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
time.sleep(2)
# OR
# act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# Ctrol+C

act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Press Tab Button
time.sleep(5)
act.send_keys(Keys.TAB)
act.perform()

# Ctrl+V
time.sleep(5)
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(5)
d.close()



