from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get('https://www.amazon.in/')
print(driver.title)
driver.find_element(By.ID,'nav-link-accountList').click()
driver.find_element(By.ID,'ap_email').send_keys('8074517920')
driver.find_element(By.ID,'continue').click()
driver.find_element(By.NAME,'password').send_keys('1235896123')
driver.find_element(By.ID,'signInSubmit').click()
driver.close()
