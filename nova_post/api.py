import requests
import importlib
from .exceptions import NovaPostApiError
from .logger import logger
from fake_useragent import UserAgent
ua = UserAgent()


class NovaPostApi:
    API_URL = "https://api.novaposhta.ua/v2.0/json/"
    DEFAULT_TIMEOUT = 10

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self._adapters_cache = {}

    def send_request(self, model: str, method: str, properties: dict, timeout: int = DEFAULT_TIMEOUT):
        headers = {
            "User-Agent": ua.random,
        }

        payload = {
            "apiKey": self.api_key,
            "modelName": model,
            "calledMethod": method,
            "methodProperties": properties
        }

        logger.info(f"Запрос: {payload}")

        try:
            response = self.session.post(self.API_URL, json=payload, timeout=timeout, headers=headers)
            result = response.json()
        except requests.Timeout:
            logger.error(f"Ошибка: запрос к {model}/{method} превысил {timeout} секунд")
            raise NovaPostApiError(f"Таймаут запроса: {timeout} секунд")
        except ValueError as e:
            logger.error("Ошибка JSON: Некорректный ответ")
            raise NovaPostApiError("Некорректный JSON ответ API")

        if not result.get('success'):
            errors = result.get('errors', ["Неизвестная ошибка API"])
            logger.error(f"Ошибка API: {errors}")
            raise NovaPostApiError(errors)

        return result['data']

    def __getattr__(self, adapter_name: str):
        if adapter_name in self._adapters_cache:
            return self._adapters_cache[adapter_name]

        try:
            module = importlib.import_module(f".adapters.{adapter_name}", package=__package__)
        except ModuleNotFoundError as e:
            raise AttributeError(f"Адаптер '{adapter_name}' не найден.") from e

        adapter_class_name = adapter_name.capitalize()
        adapter_class = getattr(module, adapter_class_name, None)

        if not adapter_class:
            raise AttributeError(f"Класс адаптера '{adapter_class_name}' не найден.")

        adapter_instance = adapter_class(self)
        self._adapters_cache[adapter_name] = adapter_instance
        return adapter_instance
