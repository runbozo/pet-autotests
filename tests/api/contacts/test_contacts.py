import pytest
import allure

from copy import deepcopy
from src.utils import fake_mail
from src.utils import CommonSteps
from src.api.models.contacts_schemas import ContactBodyModel


#test-data
create_body = ContactBodyModel().dict(exclude_none=True)


@pytest.mark.smoke
class TestContacts:

    @allure.title("Добавить новый контакт: только обязательные параметры")
    def test_add_user_required_params_only(self, contacts_client):
        body = deepcopy(create_body)
        body["email"] = fake_mail()
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
    def test_add_user_without_required_params(self, contacts_client, param, value):
        body = deepcopy(create_body)
        body[param] = value

        response = contacts_client.add_contact(body)

        with CommonSteps.STATUS_400:
            assert response.status_code == 400

    @allure.title("Добавить новый контакт: использование необязательных параметров")
    def test_add_user_additional_params(self, contacts_client):
        body = ContactBodyModel(email=fake_mail(),
                                first_name="test",
                                last_name="testovich",
                                phone="+79990001101",
                                country="Russia",
                                city="Moscow",
                                address="117535 Leningradsky Ave, 61/1",
                                ).dict()
        response = contacts_client.add_contact(body)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Получить контакт по id")
    def test_get_user(self, contacts_client, fake_contact):
        response = contacts_client.get_contact(fake_contact)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Получить контакт по id: несуществующий id")
    def test_get_user_nonexistent_id(self, contacts_client):
        response = contacts_client.get_contact("test")

        with CommonSteps.STATUS_404:
            assert response.status_code == 404

    @allure.title("Получить список всех контактов")
    def test_list_contacts(self, contacts_client, fake_contact):
        response = contacts_client.list_contacts()

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

        # TODO: валидация схемы

    @allure.title("Обновление информации о контакте")
    def test_update_contact(self, contacts_client, fake_contact):
        data = {"first_name": "test"}
        response = contacts_client.update_contact(fake_contact, data)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Обновление информации о контакте: несуществующий id")
    def test_update_contact(self, contacts_client):
        data = {"first_name": "test"}
        response = contacts_client.update_contact("test", data)

        with CommonSteps.STATUS_404:
            assert response.status_code == 404

    @allure.title("Удаление контакта по id")
    def test_delete_contact(self, contacts_client, fake_contact):
        response = contacts_client.delete_contact(fake_contact)

        with CommonSteps.STATUS_200:
            assert response.status_code == 200

    @allure.title("Удаление контакта: несуществующий id")
    def test_delete_contact_nonexistent_id(self, contacts_client):
        response = contacts_client.delete_contact("test")

        with CommonSteps.STATUS_404:
            assert response.status_code == 404
