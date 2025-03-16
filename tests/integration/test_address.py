import os

import pytest
from dotenv import load_dotenv

from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError
from nova_post.logger import logger
from nova_post.models.address import AddressUpdateRequest, AddressSaveRequest, AddressDeleteRequest

load_dotenv()


@pytest.fixture
def api():
    api_key = os.getenv("NOVA_POST_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан API-ключ для интеграционных тестов!")
    return NovaPostApi(api_key)


def test_get_cities(api):
    try:
        cities = api.address.get_cities()
        assert len(cities) > 0
        logger.info(cities[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_warehouses(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        warehouses = api.address.get_warehouses(city_ref)
        assert len(warehouses) > 0
        logger.info(warehouses[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_warehouse(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    warehouse_number = "1"
    try:
        warehouse = api.address.get_warehouse(city_ref, warehouse_number)
        assert warehouse is not None
        assert warehouse.Number == warehouse_number
        logger.info(warehouse)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_streets(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        streets = api.address.get_streets(city_ref)
        assert len(streets) > 0
        logger.info(streets[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_areas(api):
    """Тест получения списка областей"""
    try:
        areas = api.address.get_areas()
        assert len(areas) > 0
        logger.info(areas[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_cities_with_filter(api):
    try:
        cities = api.address.get_cities(find_by_string="Київ", limit=5)
        assert len(cities) > 0
        assert "Київ" in cities[0].Description
        logger.info(cities)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_streets_with_filter(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        streets = api.address.get_streets(city_ref, find_by_string="Шевченка", limit=5)
        assert len(streets) > 0
        logger.info(streets)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_city_by_ref(api):
    """Тест поиска города по Ref"""
    cities = api.address.get_cities()
    assert len(cities) > 0, "Список городов пуст!"

    city_ref = cities[0].Ref  # Берём Ref первого города
    city = api.address.get_cities(ref=city_ref)

    assert len(city) == 1, "Город с данным Ref не найден!"
    assert city[0].Ref == city_ref
    logger.info(city[0])


def test_get_warehouse_by_ref(api):
    """Тест поиска отделения по Ref"""
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    warehouses = api.address.get_warehouses(city_ref, limit=5)

    assert len(warehouses) > 0, "Список отделений пуст!"

    warehouse_ref = warehouses[0].CityRef  # Берём Ref первого отделения
    warehouse = api.address.get_warehouse(warehouse_ref)

    assert warehouse is not None, "Отделение с данным Ref не найдено!"
    logger.info(warehouse)


def test_get_street_by_ref(api):
    """Тест поиска улицы по Ref"""
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    streets = api.address.get_streets(city_ref, limit=5)

    assert len(streets) > 0, "Список улиц пуст!"

    street_ref = streets[0].Ref  # Берём Ref первой улицы
    street = api.address.get_streets(city_ref, ref=street_ref)

    assert len(street) == 1, "Улица с данным Ref не найдена!"
    assert street[0].Ref == street_ref
    logger.info(street[0])


def test_create_update_delete_address(api):
    """
    Ищем контрагента «Тестов Тест Тестович» (или любой, у кого есть контактное лицо
    с телефоном +380 (99) 123-45-67), берём его Ref, затем создаём, обновляем и удаляем адрес.
    """
    target_name = 'Тест'
    found_counterparty_ref = None

    try:
        all_counterparties = api.counterparty.get_counterparties(
            counterparty_property="Recipient",
            find_by_string="Приватна"  # ищем по строке "Тестов", чтобы быстрее сузить выборку
        )
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при запросе контрагентов: {exc}")

    for cparty in all_counterparties:
        # Загружаем контакты для данного контрагента
        contact_persons = api.counterparty.get_counterparty_contact_persons(cparty.Ref)
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

    try:
        cities = api.address.get_cities(find_by_string="Київ", limit=1)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при получении городов: {exc}")

    assert len(cities) > 0, "Не нашли ни одного города по запросу 'Київ'!"
    city_ref = cities[0].Ref

    try:
        streets = api.address.get_streets(city_ref=city_ref, limit=1)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при получении улиц: {exc}")

    assert len(streets) > 0, f"Не нашли улицу в городе {city_ref}!"
    street_ref = streets[0].Ref

    try:
        save_data = AddressSaveRequest(
            CounterpartyRef=found_counterparty_ref,
            StreetRef=street_ref,
            BuildingNumber="12Б",
            Flat="7",
            Note="Тестовый адрес (автотест)"
        )
        save_response = api.address.save_address(save_data)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при создании адреса: {exc}")

    assert save_response.Ref, "Не удалось создать адрес — API вернул пустой Ref!"
    address_ref = save_response.Ref
    logger.info(f"[TEST] Создан адрес для контрагента {found_counterparty_ref} => Ref={address_ref}")

    try:
        update_data = AddressUpdateRequest(
            Ref=address_ref,
            CounterpartyRef=found_counterparty_ref,
            StreetRef=street_ref,
            BuildingNumber="12Б",
            Flat="7",
            Note="Обновлённый автотестовый адрес"
        )
        update_response = api.address.update_address(update_data)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при обновлении адреса: {exc}")

    # assert update_response.Ref == address_ref, "Не совпадает Ref при обновлении адреса!"
    logger.info(f"[TEST] Адрес обновлён => Ref={update_response.Ref}, Description={update_response.Description}")

    delete_address = AddressDeleteRequest(
        Ref=address_ref,
    )
    try:
        is_deleted = api.address.delete_address(delete_address)
    except NovaPostApiError as exc:
        pytest.fail(f"Ошибка при удалении адреса: {exc}")

    assert is_deleted, "API вернулось пустое значение при удалении адреса!"
    logger.info(f"[TEST] Адрес удалён => Ref={address_ref}")
