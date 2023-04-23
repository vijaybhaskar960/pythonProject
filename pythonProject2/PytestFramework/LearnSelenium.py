from selenium import webdriver
from selenium.webdriver.common.by import By


class LearnSelenium:

    close_button = '//button[@class="_2KpZ6l _2doB4z"]'
    menu_items = '//div[@class="eFQ30H"]'
    menu_items_name = './/div[@class="xtXmba"]'

    def __init__(self,driver):
        self.driver = driver


    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.close_button).click()

    def get_all_menu_items_names(self):
        menu_items = self.driver.find_elements(By.XPATH, self.menu_items)
        for menu in menu_items:
            print(menu.find_element(By.XPATH, self.menu_items_name).text)

    def close_browser(self):
        self.driver.close()