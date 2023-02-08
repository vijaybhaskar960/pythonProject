from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get("https://www.myntra.com/")

windows = driver.window_handles
print("Default title is:",windows)

driver.switch_to.window(windows[0])
print("First tab title is:",driver.title)

driver.switch_to.window(windows[1])
print("Second tab title is:",driver.title)

driver.switch_to.window(windows[0])
print("Third tab title is:",driver.title)

driver.quit()

