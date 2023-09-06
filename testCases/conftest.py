import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser=='Firefox':
        driver = webdriver.Firefox(service=Service())
        driver.implicitly_wait(10)
        driver.maximize_window()
    else:
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# generate html test report
