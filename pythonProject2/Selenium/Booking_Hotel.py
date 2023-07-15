from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, '//a[@class="close"]').click()
start = driver.find_element(By.ID, "BE_flight_origin_city")
start.click()
start.send_keys("Bangalore")
start.send_keys(Keys.ENTER)

end = driver.find_element(By.ID, "BE_flight_arrival_city")
end.click()
end.send_keys("Goa")

search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

for result in search_results:
    print(result.text)
    if "Goa (GOI)" in result.text:
        result.click()
        time.sleep(3)
        break

driver.find_element(By.ID, "BE_flight_origin_date").click()
time.sleep(3)
all_dates = driver.find_elements(By.XPATH, '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')

for dates in all_dates:
    if dates.get_attribute('data-date') == "30/03/2023":
        dates.click()
        break

time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@data-flightagegroup='child']//span[@class='ddSpinnerPlus']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@class='enabled _msddli_ selected']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
time.sleep(10)

driver.close()







