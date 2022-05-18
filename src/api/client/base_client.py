import time
from typing import List

import allure
from requests import Request, Response, Session

from src.api.logger import LOGGER


class BaseClient:
    listen_response = False

    def __init__(self, base_url: str = "", default_headers: dict = {}):
        self.base_url = base_url
        self.s = Session()
        self.s.headers = default_headers

    def url_join(self, base_url, relative_url):
        url = base_url if base_url.endswith("/") else base_url + "/"
        url += relative_url[1:] if relative_url.startswith("/") else relative_url
        return url

    def prepare_request(self, method, url, **kwargs):
        request = Request(method, url, **kwargs)
        return self.s.prepare_request(request)

    def make_request(self, method, relative_url, **kwargs):

        url = self.url_join(self.base_url, relative_url)

        with allure.step(f"{method} {url}"):
            with allure.step(f"session headers = {self.s.headers}"):
                pass

            log_msg = "{} :: Выполняем запрос {} {}\n\t|> session headers = {}\n\t|>".format(
                self.__class__.__name__, method, url, self.s.headers
            )
            for k, v in kwargs.items():
                v_ = str(v)[:1000]
                with allure.step(f"{k} = {v_}"):
                    log_msg += f"\n\t|> {k} = {v_}"

            LOGGER.info(log_msg)

            prepped = self.prepare_request(method, url, **kwargs)
            response = self.s.send(prepped)
            LOGGER.info(f"Ответ: {response.text}")
            allure.attach(response.text, "Ответ:", allure.attachment_type.TEXT)

            return response
