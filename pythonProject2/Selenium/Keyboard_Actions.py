import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.facebook.com/login/')
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("VijayaReddy")
act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
act.send_keys(Keys.ENTER).perform()
time.sleep(5)
# act.key_down(Keys.CONTROL).send_keys('a')\
#     .key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)\
#     .send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()
#


driver.close()
