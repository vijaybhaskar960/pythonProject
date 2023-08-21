import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    actual_title = driver.title
    expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert actual_title.__eq__(expected_title)
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphones14")
    driver.find_element(By.ID, 'nav-search-submit-button').click()
    time.sleep(3)
    driver.quit()


