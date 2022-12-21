from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
d = webdriver.Chrome()
d.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
d.maximize_window()
d.find_element(By.XPATH,'//*[@id="table-files"]/tbody/tr[2]/td[5]/a').click()

# d.find_element(By.XPATH,'//*[@id="dismiss-button"]/div/span').click()
alert = d.switch_to.alert
alert.dismiss()
sleep(10)
d.close()