import allure
import random
from uuid import uuid4


def fake_mail():
    svc = ["gmail.com", "mail.ru", "yahoo.com", "vk.com"]

    svc = random.choice(svc)
    mail = str(uuid4())[:6] + "@" + svc
    return mail


class CommonSteps:

    STATUS_200 = allure.step("Проверить код ответа сервера status_code == 200")
    STATUS_400 = allure.step("Проверить код ответа сервера status_code == 400")
    STATUS_404 = allure.step("Проверить код ответа сервера status_code == 404")

    def custom_status(self, code):
        return allure.step(f"Проверить код ответа сервера == {code}")
