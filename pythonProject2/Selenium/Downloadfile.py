from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(3)

# Download txt file
driver.find_element(By.ID, "textbox").send_keys("testing download text file")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID,"link-to-download").click()

# Download pdf file

driver.find_element(By.ID, "pdfbox").send_keys("testing pdf")
driver.find_element(By.ID,'createPdf').click()
driver.find_element(By.ID, 'pdf-link-to-download').click()

