import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    browser = webdriver.Chrome(request.config.getoption('--chromedriver'))
    browser.implicitly_wait(5)
    yield browser
    browser.close()
