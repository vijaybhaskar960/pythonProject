from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d = webdriver.Chrome()

d.get("https://www.techlistic.com/p/demo-selenium-practice.html")
d.maximize_window()
d.execute_script("window.scrollTo(0,800)")
time.sleep(5)
table = d.find_element(By.XPATH,'//*[@id="post-body-5867683659713562481"]/div[1]/div[4]')
time.sleep(5)
header = table.find_elements(By.TAG_NAME,"tbody")
cell = table.find_elements(By.TAG_NAME,"th")

for i in header:
    print(i.text)

for i in cell:
    print(i.text)

d.close()
