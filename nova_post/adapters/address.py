from ..models.address import City, Warehouse, Street, Area, Settlement
from typing import List, Optional


class Address:
    def __init__(self, api):
        self.api = api

    def get_cities(self, find_by_string: Optional[str] = None, limit: Optional[int] = None) -> List[City]:
        """Получение списка городов"""
        properties = {}
        if find_by_string:
            properties["FindByString"] = find_by_string
        if limit:
            properties["Limit"] = limit

        result = self.api.send_request("Address", "getCities", properties)
        return [City(**city) for city in result]

    def get_warehouses(self, city_ref: str, limit: Optional[int] = None) -> List[Warehouse]:
        """Получение списка отделений"""
        properties = {"CityRef": city_ref}
        if limit:
            properties["Limit"] = limit

        result = self.api.send_request("Address", "getWarehouses", properties)
        return [Warehouse(**wh) for wh in result]

    def get_warehouse(self, city_ref: str, warehouse_number: str) -> Optional[Warehouse]:
        """Получение конкретного отделения"""
        properties = {"CityRef": city_ref, "WarehouseNumber": warehouse_number}
        result = self.api.send_request("Address", "getWarehouses", properties)
        return Warehouse(**result[0]) if result else None

    def get_streets(self, city_ref: str, find_by_string: Optional[str] = None, limit: Optional[int] = None) -> List[
        Street]:
        """Получение списка улиц"""
        properties = {"CityRef": city_ref}
        if find_by_string:
            properties["FindByString"] = find_by_string
        if limit:
            properties["Limit"] = limit

        result = self.api.send_request("Address", "getStreet", properties)
        return [Street(**street) for street in result]

    def get_areas(self) -> List[Area]:
        """Получение списка областей"""
        properties = {}
        result = self.api.send_request("Address", "getAreas", properties)
        return [Area(**area) for area in result]

    # TODO Настроить правильное возвращение get_settlements
