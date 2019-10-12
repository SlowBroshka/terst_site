import pytest
import os

from selenium import webdriver

DRIVER = str()

if os.name == 'posix':
    DRIVER = 'Drivers/chromedriver'
else:
    DRIVER = 'Drivers\\chromedriver.exe'

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if lang:
        print("\nstart test with lang: {}".format(lang))
    else:
        raise pytest.UsageError("--language should not be empty")
    browser = webdriver.Chrome(DRIVER)
    yield browser
    browser.quit()