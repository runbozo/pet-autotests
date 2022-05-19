import allure
from selenium.webdriver.common.by import By

from src.web.page.base_page import BasePage


class MailRuHome(BasePage):
    """
    Домашняя страница mail.ru
    """

    BASE_URL_PATH = "http://go.mail.ru"
    RELATIVE_URL_PATH = "/"
    STANDART_SUGGESTION_COUNT = 10

    def __init__(self, browser):
        self.browser = browser
        self.container = (By.XPATH, "//*[@id='section-main']")
        self.search_bar = (By.XPATH, "//*[@id='MSearch']/input[1]")
        self.suggestions = (By.XPATH, "//div[@class='DesktopSuggests-suggestsContainer']")
        self.suggestion_row = (By.XPATH, "//li[@class='DesktopSuggests-row']")
        self.selected_suggestion_row = (By.XPATH, "//li[@class='DesktopSuggests-row DesktopSuggests-selected']")
        self.first_row = (By.XPATH, "//li[@class='DesktopSuggests-row'] [1]")

    @allure.step("Ждём отображения сервиса")
    def wait_for_open(self):
        self.browser.find_element(*self.container)
        return self

    def fill_search_field(self, text):
        with allure.step(f"Заполнить поисковую строку текстом {text}"):
            bar = self.browser.find_element(*self.search_bar)
            bar.click()
            bar.send_keys(text)
