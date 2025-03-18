from typing import List

from ..models.address import (
    City, Warehouse, Street, Area, AddressSaveRequest, AddressUpdateRequest, AddressDeleteRequest, AddressResponse,
    SearchSettlementsRequest, SearchSettlementsResponse, SearchSettlementStreetsRequest,
    SearchSettlementStreetsResponse, GetCitiesRequest, GetWarehousesRequest, GetStreetsRequest
)


class Address:
    """
    Адаптер для роботи з адресами та адресами контрагентів.

    Дозволяє створювати, оновлювати, видаляти адреси, отримувати довідники населених пунктів, вулиць, складів тощо.
    """

    def __init__(self, api):
        self.api = api

    def save_address(self, data: AddressSaveRequest) -> AddressResponse:
        """
        Створення адреси контрагента.

        :param data: Pydantic-модель `AddressSaveRequest`, що містить дані для збереження адреси.
        :return: Об'єкт `AddressResponse` із деталями створеної адреси.
        """
        result = self.api.send_request("Address", "save", data.model_dump(exclude_unset=True))
        return AddressResponse.model_validate(result[0]) if result else AddressResponse(Ref="", Description="")

    def update_address(self, data: AddressUpdateRequest) -> AddressResponse:
        """
        Оновлення даних адреси контрагента.

        :param data: Pydantic-модель `AddressUpdateRequest`, що містить оновлені дані адреси.
        :return: Об'єкт `AddressResponse` із оновленою інформацією.
        """
        result = self.api.send_request("Address", "update", data.model_dump(exclude_unset=True))
        return AddressResponse.model_validate(result[0]) if result else AddressResponse(Ref="", Description="")

    def delete_address(self, data: AddressDeleteRequest) -> bool:
        """
        Видалення адреси контрагента.

        :param data: Pydantic-модель `AddressDeleteRequest`, що містить `Ref` адреси для видалення.
        :return: `True`, якщо адреса успішно видалена.
        """
        result = self.api.send_request("Address", "delete", data.model_dump(exclude_unset=True))
        return bool(result)

    def get_cities(self, data: GetCitiesRequest) -> List[City]:
        """
        Отримання списку міст.

        :param data: Pydantic-модель `GetCitiesRequest`, що містить параметри фільтрації.
        :return: Список об'єктів `City` із деталями міст.
        """
        result = self.api.send_request("Address", "getCities", data.model_dump(exclude_unset=True))
        return [City.model_validate(city) for city in result]

    def get_warehouses(self, data: GetWarehousesRequest) -> List[Warehouse]:
        """
        Отримання списку відділень.

        :param data: Pydantic-модель `GetWarehousesRequest`, що містить параметри фільтрації.
        :return: Список об'єктів `Warehouse` із деталями відділень.
        """
        result = self.api.send_request("Address", "getWarehouses", data.model_dump(exclude_unset=True))
        return [Warehouse.model_validate(wh) for wh in result]

    def get_streets(self, data: GetStreetsRequest) -> List[Street]:
        """
        Отримання списку вулиць.

        :param data: Pydantic-модель `GetStreetsRequest`, що містить параметри фільтрації.
        :return: Список об'єктів `Street` із назвами вулиць.
        """
        result = self.api.send_request("Address", "getStreet", data.model_dump(exclude_unset=True))
        return [Street.model_validate(street) for street in result]

    def get_areas(self) -> List[Area]:
        """
        Отримання списку областей.

        :return: Список об'єктів `Area`, що містять інформацію про області.
        """
        result = self.api.send_request("Address", "getAreas", {})
        return [Area.model_validate(area) for area in result]

    def search_settlements(self, data: SearchSettlementsRequest) -> SearchSettlementsResponse:
        """
        Онлайн-пошук населених пунктів.

        :param data: Pydantic-модель `SearchSettlementsRequest`, що містить назву або поштовий індекс міста.
        :return: Об'єкт `SearchSettlementsResponse` із результатами пошуку.
        """
        result = self.api.send_request("Address", "searchSettlements", data.model_dump(exclude_unset=True))
        if not result:
            return SearchSettlementsResponse(TotalCount="0", Addresses=[])
        return SearchSettlementsResponse.model_validate(result[0])

    def search_settlement_streets(self, data: SearchSettlementStreetsRequest) -> SearchSettlementStreetsResponse:
        """
        Онлайн-пошук вулиць у вибраному населеному пункті.

        :param data: Pydantic-модель `SearchSettlementStreetsRequest`, що містить `SettlementRef` населеного пункту.
        :return: Об'єкт `SearchSettlementStreetsResponse` із результатами пошуку.
        """
        result = self.api.send_request("Address", "searchSettlementStreets", data.model_dump(exclude_unset=True))
        if not result:
            return SearchSettlementStreetsResponse(TotalCount="0", Addresses=[])
        return SearchSettlementStreetsResponse.model_validate(result[0])
