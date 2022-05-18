import allure
from requests import Response

from src.api.client.base_client import BaseClient


class ContactsClient(BaseClient):

    URL = "api/contacts"

    def list_contacts(self) -> Response:
        allure.dynamic.label("Endpoints", self.URL)
        with allure.step("Получить список контактов"):
            return self.make_request("GET", self.URL)

    def get_contact(self, contact_id) -> Response:
        allure.dynamic.label("Endpoints", self.URL)
        with allure.step(f"Получить контакт по id {contact_id}"):
            return self.make_request("GET", self.URL + f"/{contact_id}")

    def delete_contact(self, contact_id) -> Response:
        allure.dynamic.label("Endpoints", self.URL)
        with allure.step(f"Удалить контакт по id {contact_id}"):
            return self.make_request("DELETE", self.URL + f"/{contact_id}")

    def add_contact(self, data) -> Response:
        allure.dynamic.label("Endpoints", self.URL)
        with allure.step("Добавить новый контакт"):
            return self.make_request("POST", self.URL, json=data)

    def update_contact(self, contact_id, data) -> Response:
        allure.dynamic.label("Endpoints", self.URL)
        with allure.step("Обновить информацию о контакте"):
            return self.make_request("PUT", self.URL + f"/{contact_id}", json=data)
