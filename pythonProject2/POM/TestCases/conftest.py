import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
            driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
        
    return driver


def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")



