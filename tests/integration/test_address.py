import os
import pytest
from dotenv import load_dotenv
from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError

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
        print(cities[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_warehouses(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        warehouses = api.address.get_warehouses(city_ref)
        assert len(warehouses) > 0
        print(warehouses[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_warehouse(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    warehouse_number = "1"
    try:
        warehouse = api.address.get_warehouse(city_ref, warehouse_number)
        assert warehouse is not None
        assert warehouse.Number == warehouse_number
        print(warehouse)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_streets(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        streets = api.address.get_streets(city_ref)
        assert len(streets) > 0
        print(streets[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_areas(api):
    """Тест получения списка областей"""
    try:
        areas = api.address.get_areas()
        assert len(areas) > 0
        print(areas[0])
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_cities_with_filter(api):
    try:
        cities = api.address.get_cities(find_by_string="Київ", limit=5)
        assert len(cities) > 0
        assert "Київ" in cities[0].Description
        print(cities)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_streets_with_filter(api):
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    try:
        streets = api.address.get_streets(city_ref, find_by_string="Шевченка", limit=5)
        assert len(streets) > 0
        print(streets)
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
    print(city[0])


def test_get_warehouse_by_ref(api):
    """Тест поиска отделения по Ref"""
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    warehouses = api.address.get_warehouses(city_ref, limit=5)

    assert len(warehouses) > 0, "Список отделений пуст!"

    warehouse_ref = warehouses[0].CityRef  # Берём Ref первого отделения
    warehouse = api.address.get_warehouse(warehouse_ref)

    assert warehouse is not None, "Отделение с данным Ref не найдено!"
    print(warehouse)


def test_get_street_by_ref(api):
    """Тест поиска улицы по Ref"""
    city_ref = "8d5a980d-391c-11dd-90d9-001a92567626"  # Код Киева
    streets = api.address.get_streets(city_ref, limit=5)

    assert len(streets) > 0, "Список улиц пуст!"

    street_ref = streets[0].Ref  # Берём Ref первой улицы
    street = api.address.get_streets(city_ref, ref=street_ref)

    assert len(street) == 1, "Улица с данным Ref не найдена!"
    assert street[0].Ref == street_ref
    print(street[0])

# TODO Настроить тесты для get_settlements
