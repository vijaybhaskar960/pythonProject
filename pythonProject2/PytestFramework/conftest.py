import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")




# @pytest.fixture()
# def setup():
#     print("Before a test case Starting")
#     yield
#     print("After Every Test Case")

# Using the conftest file common methods kept into this file no need write  to every test case

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Before a test case Starting")
    yield
    print("After Every Test Case")

#
# @pytest.fixture(params=["chrome", 'firefox', 'edge'])
# #@pytest.fixture()
# def setup_and_teardown(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     # elif request.param == 'firefox':
#     #     driver = webdriver.Firefox()
#     # elif request.param == "edge":
#     #     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.get("https://www.amazon.in/")
#     request.cls.driver = driver
#     yield
#     driver.quit()


@pytest.fixture()
def setup_and_teardown(request):
    global driver

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver
    yield
    driver.quit()
