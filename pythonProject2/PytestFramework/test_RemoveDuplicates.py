import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_amazon_login(self):
        self.driver.find_element(By.ID, "nav-link-accountList").click()
        self.driver.find_element(By.ID, 'ap_email').send_keys("8074517920")
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, 'ap_password').send_keys("Vijayreddy123@")
        self.driver.find_element(By.ID, 'signInSubmit').click()
        actual_title = self.driver.title
        print(actual_title)
        expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        assert actual_title.__eq__(expected_title)
        allure.attach(self.driver.get_screenshot_as_png(), name="amazon_login", attachment_type=AttachmentType.PNG)


    def test_amazon_search(self):
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("iphone14")
        self.driver.find_element(By.ID, 'nav-search-submit-button').click()
        print(self.driver.title)




