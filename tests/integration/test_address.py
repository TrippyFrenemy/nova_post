import os

import pytest
from dotenv import load_dotenv

from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError
from nova_post.logger import logger
from nova_post.models.address import (
    AddressUpdateRequest, AddressSaveRequest, AddressDeleteRequest,
    GetCitiesRequest, GetWarehousesRequest, GetStreetsRequest
)
from nova_post.models.contact_person import GetContactPersonRequest
from nova_post.models.counterparty import GetCounterpartiesRequest

load_dotenv()


@pytest.fixture
def api():
    api_key = os.getenv("NOVA_POST_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан API-ключ для интеграционных тестов!")
    return NovaPostApi(api_key)


def test_get_cities(api):
    request_data = GetCitiesRequest(FindByString="Київ", Limit=5)
    try:
        cities = api.address.get_cities(request_data)
        assert len(cities) > 0
        logger.info(cities[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_warehouses(api):
    request_data = GetWarehousesRequest(CityRef="8d5a980d-391c-11dd-90d9-001a92567626", Limit=5)
    try:
        warehouses = api.address.get_warehouses(request_data)
        assert len(warehouses) > 0
        logger.info(warehouses[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_streets(api):
    request_data = GetStreetsRequest(CityRef="8d5a980d-391c-11dd-90d9-001a92567626", FindByString="Шевченка", Limit=5)
    try:
        streets = api.address.get_streets(request_data)
        assert len(streets) > 0
        logger.info(streets[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_create_update_delete_address(api):
    """
    Тест создания, обновления и удаления адреса контрагента.
    """
    target_name = 'Тест'
    found_counterparty_ref = None

    try:
        counter_party = GetCounterpartiesRequest(
            CounterpartyProperty="Recipient",
            FindByString="Приватна"
        )
        all_counterparties = api.counterparty.get_counterparties(counter_party)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при запросе контрагентов: {exc}")

    found_counterparty_ref = None
    for cparty in all_counterparties:
        # Загружаем контакты для данного контрагента
        cparty_ref = GetContactPersonRequest(Ref=cparty.Ref)
        contact_persons = api.counterparty.get_counterparty_contact_persons(cparty_ref)
        for cp in contact_persons:
            if cp.FirstName and target_name in cp.FirstName:
                found_counterparty_ref = cparty.Ref
                break
        if found_counterparty_ref:
            break

    assert found_counterparty_ref, (
        f"Не нашли контрагента с именем {target_name}. "
        "Убедитесь, что он существует или измените критерии поиска."
    )

    # Поиск города
    city_request = GetCitiesRequest(FindByString="Київ", Limit=1)
    try:
        cities = api.address.get_cities(city_request)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при получении городов: {exc}")

    assert len(cities) > 0, "Не найден город 'Київ'!"
    city_ref = cities[0].Ref

    # Поиск улицы
    street_request = GetStreetsRequest(CityRef=city_ref, Limit=1)
    try:
        streets = api.address.get_streets(street_request)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при получении улиц: {exc}")

    assert len(streets) > 0, "Не найдена улица в городе 'Київ'!"
    street_ref = streets[0].Ref

    # Создание адреса
    save_data = AddressSaveRequest(
        CounterpartyRef=found_counterparty_ref,
        StreetRef=street_ref,
        BuildingNumber="12Б",
        Flat="7",
        Note="Тестовый адрес (автотест)"
    )
    try:
        save_response = api.address.save_address(save_data)
        assert save_response.Ref, "Не удалось создать адрес — API вернул пустой Ref!"
        address_ref = save_response.Ref
        logger.info(f"[TEST] Создан адрес => Ref={address_ref}")
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при создании адреса: {exc}")

    # Обновление адреса
    update_data = AddressUpdateRequest(
        Ref=address_ref,
        CounterpartyRef=found_counterparty_ref,
        StreetRef=street_ref,
        BuildingNumber="12Б",
        Flat="7",
        Note="Обновлённый автотестовый адрес"
    )
    try:
        update_response = api.address.update_address(update_data)
        logger.info(f"[TEST] Адрес обновлён => Ref={update_response.Ref}, Description={update_response.Description}")
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при обновлении адреса: {exc}")

    # Удаление адреса
    delete_address = AddressDeleteRequest(Ref=address_ref)
    try:
        is_deleted = api.address.delete_address(delete_address)
        assert is_deleted, "API вернулось пустое значение при удалении адреса!"
        logger.info(f"[TEST] Адрес удалён => Ref={address_ref}")
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при удалении адреса: {exc}")

