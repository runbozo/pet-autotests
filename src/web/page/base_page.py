from urllib.parse import urljoin

import allure


class BasePage:

    BASE_URL_PATH = "http://"
    RELATIVE_URL_PATH = "/"

    def __init__(self, browser):
        self.browser = browser

    @property
    def url(self):
        return urljoin(self.BASE_URL_PATH, self.RELATIVE_URL_PATH)

    def navigate(self):
        with allure.step(f"Перейти на {self.url}"):
            self.browser.get(self.url)
            self.wait_for_open()
            return self

    def wait_for_open(self):
        return self
