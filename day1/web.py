
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# create webdriver object
# driver = webdriver.Chrome()

# set implicit wait time
# driver.implicitly_wait(10)  # seconds
#
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
#
# # get element after 10 seconds
# element = driver.find_element(By.PARTIAL_LINK_TEXT,"Courses")
#
# # click element
# element.click()


# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.implicitly_wait(20)
#
# driver.get("https://www.flipkart.com/")
# time.sleep(5)
#driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/p/a/img').click()
# time.sleep(4)
# driver.close()

# d = webdriver.Chrome()
# d.maximize_window()
# d.get("https://accounts.google.com/")
# time.sleep(5)
# d.execute_script("window.open('https://www.amazon.in/')")
#
# time.sleep(5)
# d.execute_script("window.open('https://www.myntra.com/')")
#
# time.sleep(5)
# d.execute_script("window.open('https://www.meesho.com/')")
#
# windows = d.window_handles
# print('\n window',windows)
# print('\n Default tab title ',d.title)
#
# d.switch_to.window(windows[1])
# print('\n window 1 tab title ',d.title)
#
# time.sleep(5)
#
# d.switch_to.window(windows[2])
# print('\n window 2 tab title ',d.title)
#
# time.sleep(5)
# d.switch_to.window(windows[3])
# print('\n window 3 tab title ',d.title)
#
# time.sleep(5)
# d.switch_to.window(windows[1])
# time.sleep(5)
# d.execute_script("document.body.style.zoom='300%'")
# time.sleep(5)
# print('\n window 1 tab title ',d.title)
#
# time.sleep(5)
# d.quit()

driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

search_link = mywait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")))
search_link.send_keys("98774372648")

password_link = mywait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input"))).send_keys("vijayreddy")
driver.close()
