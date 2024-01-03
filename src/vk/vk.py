import requests

from .exceptions import VkError


class Vk:
    def __init__(self, token: str, version: str = "5.199") -> None:
        self.token = token
        self.version = version
        self.api_url = "https://api.vk.com/method/"

    def method(self, method: str, params: dict):
        ...

    def execute(self, script: str):
        ...
