from selenium import webdriver
import pytest
from POM.PageObjects.loginpage import LoginPage
from POM.Utilities.readProperies import ReadConfig
from POM.Utilities.customLogger import LogGen


class Test_01_Login:
    baseURL = ReadConfig.getApllicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePage_Title(self, setup):

        self.logger.info("====================Verify Home Page===================")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("==============Home Page test is Passed=============")
        else:
            self.driver.save_screenshot(r"C:\Users\vijay\PycharmProjects\pythonProject2\POM\Screenshot\demo.png")
            self.driver.close()
            self.logger.error("==============Home Page test is  not Passed=============")
            assert False

    def test_login(self, setup):
        self.logger.info("====================Verify Login Page===================")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("==============Login Page test is Passed=============")
        else:
            self.driver.save_screenshot(r"C:\Users\vijay\PycharmProjects\pythonProject2\POM\Screenshot\demo1.png")
            self.driver.close()
            self.logger.error("==============Login Page test is not Passed=============")
            assert False
