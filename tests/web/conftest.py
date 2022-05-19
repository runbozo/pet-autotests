import pytest
from selenium import webdriver
#"/Users/asbelozerov/Desktop/self/pet-autotests/chromedriverz"

@pytest.fixture(scope="class")
def browser(request):
    browser = webdriver.Chrome(request.config.getoption('--chromedriver'))
    browser.implicitly_wait(5)
    yield browser
    browser.close()
