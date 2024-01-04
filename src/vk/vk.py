import requests

from .exceptions import VkError, VkResponseError, ResponseError


class Vk:
    def __init__(self, token: str, version: str = "5.199") -> None:
        self.token = token
        self.version = version
        self.api_url = "https://api.vk.com/method/"

    def request(self, url: str, data: dict, method: bool = False):
        if method:
            response = requests.post(url, data)
        else:
            response = requests.get(url, data)

        if response.status_code == 200:
            data = response.json()

            if data.get("response"):
                return data['response']
            elif data.get("error"):
                raise VkResponseError(
                    data['error']['error_code'], data['error']['error_msg']
                )
            else:
                return data
        else:
            raise ResponseError("Status code is not 200")

    def method(self, method: str, params: dict):
        ...

    def execute(self, script: str):
        ...
