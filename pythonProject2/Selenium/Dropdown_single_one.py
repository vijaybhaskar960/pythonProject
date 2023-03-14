from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
element = driver.find_element(By.ID, "RESULT_RadioButton-9")
drp = Select(element)
drp.select_by_value("Radio-1")
drp.select_by_visible_text('Evening')
print(len(drp.options))
all_options = drp.options
for option in all_options:
    print(option.text)
driver.close()