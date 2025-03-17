from typing import List, Optional

from ..models.address import (
    City, Warehouse, Street, Area, AddressSaveRequest, AddressUpdateRequest, AddressDeleteRequest, AddressResponse,
    SearchSettlementsRequest, SearchSettlementsResponse, SearchSettlementsItem,
    SearchSettlementStreetsResponse, SearchSettlementStreetsItem,
)


class Address:
    def __init__(self, api):
        self.api = api

    def save_address(self, data: AddressSaveRequest) -> AddressResponse:
        """
        Создать адрес контрагента (модель 'Address', метод 'save').
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("Address", "save", properties)
        if not result:
            return AddressResponse(Ref="", Description="")
        return AddressResponse.model_validate(result[0])

    def update_address(self, data: AddressUpdateRequest) -> AddressResponse:
        """
        Обновить данные адреса контрагента (модель 'Address', метод 'update').
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("Address", "update", properties)
        if not result:
            return AddressResponse(Ref="", Description="")
        return AddressResponse.model_validate(result[0])

    def delete_address(self, data: AddressDeleteRequest) -> bool:
        """
        Удалить адрес контрагента (модель 'Address', метод 'delete').
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("Address", "delete", properties)
        return bool(result)

    def get_cities(self, find_by_string: Optional[str] = None, ref: Optional[str] = None,
                   limit: Optional[int] = None, page: Optional[int] = None,
                   warehouse: Optional[str] = None) -> List[City]:
        """Получение списка городов (с дополнительными параметрами)."""
        properties = {}
        if find_by_string:
            properties["FindByString"] = find_by_string
        if ref:
            properties["Ref"] = ref
        if limit:
            properties["Limit"] = limit
        if page:
            properties["Page"] = page
        if warehouse:
            properties["Warehouse"] = warehouse

        result = self.api.send_request("Address", "getCities", properties)
        return [City(**city) for city in result]

    def get_warehouses(self, city_ref: Optional[str] = None,
                       warehouse_ref: Optional[str] = None,
                       limit: Optional[int] = None,
                       page: Optional[int] = None,
                       find_by_string: Optional[str] = None) -> List[Warehouse]:
        """Получение списка отделений (поиск по городу, складу или лимиту)."""
        properties = {}
        if city_ref:
            properties["CityRef"] = city_ref
        if warehouse_ref:
            properties["Ref"] = warehouse_ref
        if limit:
            properties["Limit"] = limit
        if page:
            properties["Page"] = page
        if find_by_string:
            properties["FindByString"] = find_by_string

        result = self.api.send_request("Address", "getWarehouses", properties)
        return [Warehouse(**wh) for wh in result]

    def get_warehouse(self, city_ref: str, warehouse_number: Optional[str] = None,
                      warehouse_ref: Optional[str] = None) -> Optional[Warehouse]:
        """Получение конкретного отделения."""
        properties = {"CityRef": city_ref}
        if warehouse_number:
            properties["WarehouseNumber"] = warehouse_number
        if warehouse_ref:
            properties["Ref"] = warehouse_ref
        result = self.api.send_request("Address", "getWarehouses", properties)
        return Warehouse(**result[0]) if result else None

    def get_streets(self, city_ref: str, find_by_string: Optional[str] = None,
                    ref: Optional[str] = None, limit: Optional[int] = None,
                    page: Optional[int] = None) -> List[Street]:
        """Получение списка улиц (поиск по названию, Ref или ограничение)."""
        properties = {"CityRef": city_ref}
        if find_by_string:
            properties["FindByString"] = find_by_string
        if ref:
            properties["Ref"] = ref
        if limit:
            properties["Limit"] = limit
        if page:
            properties["Page"] = page

        result = self.api.send_request("Address", "getStreet", properties)
        return [Street(**street) for street in result]

    def get_areas(self) -> List[Area]:
        """Получение списка областей."""
        result = self.api.send_request("Address", "getAreas", {})
        return [Area(**area) for area in result]

    def search_settlements(self, data: SearchSettlementsRequest) -> SearchSettlementsResponse:
        """
        Онлайн-поиск населённых пунктов (Address / searchSettlements).
        """
        properties = data.model_dump(exclude_unset=True)

        result = self.api.send_request("Address", "searchSettlements", properties)
        # result может быть массивом в data или объектом с TotalCount / Addresses
        if not result:
            return SearchSettlementsResponse(TotalCount="0", Addresses=[])
        # Обычно result[0] содержит нужный блок
        data_block = result[0]
        return SearchSettlementsResponse(
            TotalCount=data_block.get("TotalCount"),
            Addresses=[
                SearchSettlementsItem(**item) for item in data_block.get("Addresses", [])
            ]
        )

    def search_settlement_streets(self, data: SearchSettlementStreetsResponse) -> SearchSettlementStreetsResponse:
        """
        Онлайн-поиск улиц в выбранном населенном пункте (Address / searchSettlementStreets).
        """
        properties = data.model_dump(exclude_unset=True)

        result = self.api.send_request("Address", "searchSettlementStreets", properties)
        if not result:
            return SearchSettlementStreetsResponse(TotalCount="0", Addresses=[])
        # Обычно result[0] содержит Addresses, TotalCount
        data_block = result[0]
        return SearchSettlementStreetsResponse(
            TotalCount=data_block.get("TotalCount"),
            Addresses=[
                SearchSettlementStreetsItem(**item)
                for item in data_block.get("Addresses", [])
            ]
        )
