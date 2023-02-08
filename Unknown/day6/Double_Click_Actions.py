from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()

driver.switch_to.frame('iframeResult')

input = driver.find_element(By.ID,'field1')
input.clear()
input.send_keys("Welcome new world")

button = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
act = ActionChains(driver)
act.double_click(button).perform()
driver.close()
