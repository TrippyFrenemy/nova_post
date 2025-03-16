import os

import pytest
from dotenv import load_dotenv

from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError
from nova_post.logger import logger
from nova_post.models.common import TimeIntervalRequest

load_dotenv()


@pytest.fixture
def api():
    api_key = os.getenv("NOVA_POST_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан API-ключ для интеграционных тестов!")
    return NovaPostApi(api_key)


def test_get_time_intervals(api):
    request_data = TimeIntervalRequest(
        RecipientCityRef="8d5a980d-391c-11dd-90d9-001a92567626",  # Пример REF города
        # DateTime="17.03.2025"
    )
    try:
        result = api.common.get_time_intervals(request_data)
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_cargo_types(api):
    try:
        result = api.common.get_cargo_types()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_pallets_list(api):
    try:
        result = api.common.get_pallets_list()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_types_of_payers_for_redelivery(api):
    try:
        result = api.common.get_types_of_payers_for_redelivery()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_pack_list(api):
    try:
        result = api.common.get_pack_list()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_tires_wheels_list(api):
    try:
        result = api.common.get_tires_wheels_list()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_cargo_description_list(api):
    try:
        result = api.common.get_cargo_description_list()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_service_types(api):
    try:
        result = api.common.get_service_types()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")


def test_get_ownership_forms_list(api):
    try:
        result = api.common.get_ownership_forms_list()
        assert len(result) > 0
        logger.info(result[0])
    except NovaPostApiError as e:
        pytest.fail(f"Ошибка API: {e}")
