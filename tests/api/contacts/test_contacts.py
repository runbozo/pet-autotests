import pytest
import allure

from copy import deepcopy
from src.utils import fake_mail
from src.utils import CommonSteps
from src.api.models.contacts_schemas import ContactBodyModel


#test-data
create_body = ContactBodyModel().dict(exclude_none=True)


@allure.suite("Контакты API")
@pytest.mark.smoke
class TestContacts:

    @pytest.mark.positive
    @allure.title("Добавить новый контакт: только обязательные параметры")
    def test_add_user_required_params_only(self, contacts_client):
        body = deepcopy(create_body)
        body["email"] = fake_mail()

        with allure.step("Добавить контакт"):
            response = contacts_client.add_contact(body)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Добавить новый контакт без обязательных параметров")
    @pytest.mark.parametrize(
        "param, value",
        [
            ("email", None),
            ("first_name", None),
        ]
    )
    @pytest.mark.negative
    def test_add_user_without_required_params(self, contacts_client, param, value):
        body = deepcopy(create_body)
        body[param] = value

        with allure.step("Добавить контакт"):
            response = contacts_client.add_contact(body)

        with CommonSteps.STATUS_400:
            assert response.status_code == 400

    @allure.title("Получить контакт по id")
    def test_get_user(self, contacts_client, fake_contact):
        with allure.step("Получить контакт"):
            response = contacts_client.get_contact(fake_contact)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Получить контакт по id: несуществующий id")
    def test_get_user_nonexistent_id(self, contacts_client):
        response = contacts_client.get_contact("test")

        with CommonSteps.STATUS_404:
            assert response.status_code == 404

    @allure.title("Обновление информации о контакте")
    def test_update_contact(self, contacts_client, fake_contact):
        data = {"first_name": "test"}
        response = contacts_client.update_contact(fake_contact, data)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Удаление контакта по id")
    def test_delete_contact(self, contacts_client, fake_contact):
        response = contacts_client.delete_contact(fake_contact)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200
