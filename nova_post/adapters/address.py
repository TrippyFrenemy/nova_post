from typing import List, Optional
from ..models.address import (
    City, Warehouse, Street, Area, AddressSaveRequest, AddressUpdateRequest, AddressDeleteRequest, AddressResponse,
    SearchSettlementsRequest, SearchSettlementsResponse, SearchSettlementsItem,
    SearchSettlementStreetsRequest, SearchSettlementStreetsResponse, SearchSettlementStreetsItem,
    GetCitiesRequest, GetWarehousesRequest, GetStreetsRequest
)


class Address:
    def __init__(self, api):
        self.api = api

    def save_address(self, data: AddressSaveRequest) -> AddressResponse:
        """
        Создать адрес контрагента (модель 'Address', метод 'save').
        """
        result = self.api.send_request("Address", "save", data.model_dump(exclude_unset=True))
        return AddressResponse.model_validate(result[0]) if result else AddressResponse(Ref="", Description="")

    def update_address(self, data: AddressUpdateRequest) -> AddressResponse:
        """
        Обновить данные адреса контрагента (модель 'Address', метод 'update').
        """
        result = self.api.send_request("Address", "update", data.model_dump(exclude_unset=True))
        return AddressResponse.model_validate(result[0]) if result else AddressResponse(Ref="", Description="")

    def delete_address(self, data: AddressDeleteRequest) -> bool:
        """
        Удалить адрес контрагента (модель 'Address', метод 'delete').
        """
        result = self.api.send_request("Address", "delete", data.model_dump(exclude_unset=True))
        return bool(result)

    def get_cities(self, data: GetCitiesRequest) -> List[City]:
        """Получение списка городов с фильтрацией"""
        result = self.api.send_request("Address", "getCities", data.model_dump(exclude_unset=True))
        return [City.model_validate(city) for city in result]

    def get_warehouses(self, data: GetWarehousesRequest) -> List[Warehouse]:
        """Получение списка отделений с фильтрацией"""
        result = self.api.send_request("Address", "getWarehouses", data.model_dump(exclude_unset=True))
        return [Warehouse.model_validate(wh) for wh in result]

    def get_streets(self, data: GetStreetsRequest) -> List[Street]:
        """Получение списка улиц с фильтрацией"""
        result = self.api.send_request("Address", "getStreet", data.model_dump(exclude_unset=True))
        return [Street.model_validate(street) for street in result]

    def get_areas(self) -> List[Area]:
        """Получение списка областей."""
        result = self.api.send_request("Address", "getAreas", {})
        return [Area.model_validate(area) for area in result]

    def search_settlements(self, data: SearchSettlementsRequest) -> SearchSettlementsResponse:
        """
        Онлайн-поиск населённых пунктов (Address / searchSettlements).
        """
        result = self.api.send_request("Address", "searchSettlements", data.model_dump(exclude_unset=True))
        if not result:
            return SearchSettlementsResponse(TotalCount="0", Addresses=[])
        return SearchSettlementsResponse.model_validate(result[0])

    def search_settlement_streets(self, data: SearchSettlementStreetsRequest) -> SearchSettlementStreetsResponse:
        """
        Онлайн-поиск улиц в выбранном населенном пункте (Address / searchSettlementStreets).
        """
        result = self.api.send_request("Address", "searchSettlementStreets", data.model_dump(exclude_unset=True))
        if not result:
            return SearchSettlementStreetsResponse(TotalCount="0", Addresses=[])
        return SearchSettlementStreetsResponse.model_validate(result[0])
