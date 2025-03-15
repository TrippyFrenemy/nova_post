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

# TODO Настроить тесты для get_settlements
