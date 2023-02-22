import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service_obj = Service(r"C:\Users\Vijay Bhaskar Reddy\Downloads\chromedriver_win32\chromedriver.exe")


def test_google():
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10)
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.rediff.com/")
    driver.implicitly_wait(10)
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()

def test_myntra():
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.myntra.com/")
    driver.implicitly_wait(10)
    assert driver.title == "Online Shopping for Women, Men, Kids Fashion & Lifestyle - Myntra"
    driver.quit()







