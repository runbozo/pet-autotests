import pytest
import allure

from src.api.client.contacts_client import ContactsClient
from src.api.models.contacts_schemas import ContactBodyModel
from src.utils import fake_mail
from config import settings as cfg


new_user_body = ContactBodyModel(
    email=fake_mail(),
    first_name="test"
)


@pytest.fixture(scope="class")
def contacts_client():
    yield ContactsClient(base_url=cfg.base_url)


@pytest.fixture(scope="function")
def fake_contact(contacts_client):

    with allure.step("Создать запись контакта для тестов"):
        response = contacts_client.add_contact(new_user_body.dict(exclude_none=True))
    assert response.status_code == 200

    contact_id = response.json()['id']

    yield contact_id

    response = contacts_client.delete_contact(contact_id)
    assert response.status_code in (200, 404)


@pytest.fixture(scope="class", autouse=True)
def cleanup_test_contacts(contacts_client):
    yield

    with allure.step("Удаляем все записи из базы с first_name == 'test'"):
        response = contacts_client.list_contacts()
        assert response.status_code == 200

        list_contacts = response.json()
        for contact in list_contacts:
            if contact["first_name"] == "test":
                contacts_client.delete_contact(contact["id"])
