import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Launch_browsers(unittest.TestCase):

    def test_amazon(self):
        service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.get("https://www.amazon.in/")
        print(driver.title)
        act_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        if act_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
        else:
            assert False

        driver.maximize_window()
        driver.find_element(By.ID, "nav-link-accountList").click()
        driver.find_element(By.NAME, 'email').send_keys('8074517920')
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "ap_password").send_keys('vijay@gmail.com')
        driver.find_element(By.ID, 'signInSubmit').click()
        driver.close()

    def test_addition(self):
        print("this is Addition Method")



if __name__ == "__main__":
    unittest.main()