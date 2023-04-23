from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pythonProject2.PytestFramework.LearnSelenium import LearnSelenium



class TestChildLocator:

    def test_method(self):

        service_obj = Service(r"C:\Users\vijay\Downloads\chromedriver_win32\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        coding = LearnSelenium(driver)
        coding.click_close_button()
        coding.get_all_menu_items_names()
        coding.close_browser()
