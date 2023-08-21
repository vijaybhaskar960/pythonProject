import time

from selenium import webdriver

def test_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    print(driver.title)
    time.sleep(3)
    driver.quit()


def test_flipkart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    print(driver.title)
    time.sleep(2)
    driver.quit()

def test_myntra():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.myntra.com/")
    print(driver.title)
    time.sleep(2)
    driver.quit()

def test_new():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://omayo.blogspot.com/")
    print(driver.title)
    time.sleep(3)
    driver.quit()

