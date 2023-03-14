from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(3)
start = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
start.click()
time.sleep(3)
start.send_keys("New Delhi")
time.sleep(2)
start.send_keys(Keys.ENTER)
time.sleep(3)
end = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
end.click()
end.send_keys("New York")
time.sleep(3)

search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
print(len(search_results))

for results in search_results:
    print(results.text)
    if "New York (JFK)" in results.text:
        results.click()
        time.sleep(3)
        break


origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
origin.click()
time.sleep(3)
all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

for dates in all_dates:
    if dates.get_attribute("data-date") == "25/03/2023":
        dates.click()
        time.sleep(3)
        break





