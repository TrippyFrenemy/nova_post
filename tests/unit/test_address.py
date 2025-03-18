import pytest
from unittest.mock import Mock

from nova_post.api import NovaPostApi
from nova_post.models.address import (
    AddressUpdateRequest, AddressSaveRequest, AddressDeleteRequest,
    GetCitiesRequest, GetWarehousesRequest, GetStreetsRequest
)


@pytest.fixture
def mock_api():
    api = Mock(spec=NovaPostApi)
    api.address = Mock()
    return api


def test_get_cities(mock_api):
    mock_response = [Mock(Ref="city1"), Mock(Ref="city2")]
    mock_api.address.get_cities.return_value = mock_response

    request = GetCitiesRequest(FindByString="Київ", Limit=5)
    response = mock_api.address.get_cities(request)

    assert len(response) == 2
    assert response[0].Ref == "city1"
    assert response[1].Ref == "city2"
    mock_api.address.get_cities.assert_called_once_with(request)


def test_get_warehouses(mock_api):
    mock_response = [Mock(Ref="wh1"), Mock(Ref="wh2")]
    mock_api.address.get_warehouses.return_value = mock_response

    request = GetWarehousesRequest(CityRef="city-ref-123", Limit=5)
    response = mock_api.address.get_warehouses(request)

    assert len(response) == 2
    assert response[0].Ref == "wh1"
    assert response[1].Ref == "wh2"
    mock_api.address.get_warehouses.assert_called_once_with(request)


def test_get_streets(mock_api):
    mock_response = [Mock(Ref="st1"), Mock(Ref="st2")]
    mock_api.address.get_streets.return_value = mock_response

    request = GetStreetsRequest(CityRef="city-ref-123", FindByString="Шевченка", Limit=5)
    response = mock_api.address.get_streets(request)

    assert len(response) == 2
    assert response[0].Ref == "st1"
    assert response[1].Ref == "st2"
    mock_api.address.get_streets.assert_called_once_with(request)


def test_create_update_delete_address(mock_api):
    # Mock создания адреса
    mock_save_response = Mock(Ref="addr-ref-123")
    mock_api.address.save_address.return_value = mock_save_response

    save_request = AddressSaveRequest(
        CounterpartyRef="cp-ref-123", StreetRef="st-ref-123", BuildingNumber="12Б", Flat="7", Note="Тестовый адрес"
    )
    save_response = mock_api.address.save_address(save_request)

    assert save_response.Ref == "addr-ref-123"
    mock_api.address.save_address.assert_called_once_with(save_request)

    # Mock обновления адреса
    mock_update_response = Mock(Ref="addr-ref-123", Description="Обновленный адрес")
    mock_api.address.update_address.return_value = mock_update_response

    update_request = AddressUpdateRequest(
        Ref="addr-ref-123", Note="Обновлённый автотестовый адрес"
    )
    update_response = mock_api.address.update_address(update_request)

    assert update_response.Ref == "addr-ref-123"
    assert update_response.Description == "Обновленный адрес"
    mock_api.address.update_address.assert_called_once_with(update_request)

    # Mock удаления адреса
    mock_api.address.delete_address.return_value = True

    delete_request = AddressDeleteRequest(Ref="addr-ref-123")
    delete_response = mock_api.address.delete_address(delete_request)

    assert delete_response is True
    mock_api.address.delete_address.assert_called_once_with(delete_request)
