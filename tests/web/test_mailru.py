import allure
import pytest

from src.web.page.mailru_page import MailRuHome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.web
class TestMailRuHomepage:

    @allure.title("Появление suggestion при клике на поисковую строку")
    def test_appearance_suggestion(self, browser):
        home_page = MailRuHome(browser).navigate()
        home_page.fill_search_field("test")

        with allure.step("Убедиться в появлении suggestions на странице"):
            assert browser.find_element(*home_page.suggestions)

    @allure.title("Количество элементов в suggestion")
    def test_suggestion_rows_count(self, browser):
        home_page = MailRuHome(browser).navigate()
        home_page.fill_search_field("test")

        with allure.step(f"Убедиться, что кол-во строк suggestions == {home_page.STANDART_SUGGESTION_COUNT}"):
            suggestion_rows = browser.find_elements(*home_page.suggestion_row)
            assert len(suggestion_rows) == home_page.STANDART_SUGGESTION_COUNT

    @allure.title("Выделение suggestion строки при наведении курсора")
    def test_suggestion_rows_selected(self, browser):
        home_page = MailRuHome(browser).navigate()
        home_page.fill_search_field("test")
        first_row = browser.find_element(*home_page.first_row)

        hover = ActionChains(browser).move_to_element(first_row)
        hover.perform()

        with allure.step("Убедиться в наличии css-класса selected у наведенного эелемента"):
            selected_row = browser.find_elements(*home_page.selected_suggestion_row)
            assert len(selected_row) == 1

    @allure.title("Сокрытие suggestions по горячей клавише 'ESC'")
    def test_suggestions_hide_hotkey(self, browser):
        home_page = MailRuHome(browser).navigate()
        home_page.fill_search_field("test")

        with allure.step("Убедиться в появлении suggestions на странице"):
            assert browser.find_element(*home_page.suggestions)

        with allure.step("Нажать горячую клавишу 'Esc'"):
            bar = browser.find_element(*home_page.search_bar)
            bar.send_keys(Keys.ESCAPE)

        with allure.step("Убедиться в отсутствии suggestions на странице"):
            assert not browser.find_elements(*home_page.suggestions)
