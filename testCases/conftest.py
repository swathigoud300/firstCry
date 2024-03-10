import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'Edge':
        driver = webdriver.Edge()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


