from typing import Optional, List

from pydantic import BaseModel


class City(BaseModel):
    """Модель города"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Area: Optional[str] = None


class Warehouse(BaseModel):
    """Модель отделения"""
    SiteKey: int
    Description: str
    DescriptionRu: Optional[str] = None
    Number: str
    CityRef: str
    TypeOfWarehouse: Optional[str] = None


class Street(BaseModel):
    """Модель улицы"""
    Ref: str
    Description: str
    StreetsTypeRef: str
    StreetsType: str


class Area(BaseModel):
    """Модель области"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None


class Settlement(BaseModel):
    """Модель населённого пункта"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    AreaRef: str
    Type: str


class AddressSaveRequest(BaseModel):
    """Модель для создания адреса."""
    CounterpartyRef: str
    StreetRef: str
    BuildingNumber: str
    Flat: Optional[str] = None
    Note: Optional[str] = None


class AddressUpdateRequest(BaseModel):
    """Модель для обновления адреса."""
    Ref: str
    CounterpartyRef: Optional[str] = None
    StreetRef: Optional[str] = None
    BuildingNumber: Optional[str] = None
    Flat: Optional[str] = None
    Note: Optional[str] = None


class AddressDeleteRequest(BaseModel):
    """Модель для удаления адреса."""
    Ref: str


class AddressResponse(BaseModel):
    """Ответ при создании / обновлении / удалении адреса."""
    Ref: str
    Description: Optional[str] = None


class GetCitiesRequest(BaseModel):
    """Модель запроса списка городов."""
    FindByString: Optional[str] = None
    Ref: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None
    Warehouse: Optional[str] = None


class GetWarehousesRequest(BaseModel):
    """Модель запроса списка отделений."""
    CityRef: Optional[str] = None
    WarehouseRef: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None
    FindByString: Optional[str] = None


class GetStreetsRequest(BaseModel):
    """Модель запроса списка улиц."""
    CityRef: str
    FindByString: Optional[str] = None
    Ref: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None


class SearchSettlementsRequest(BaseModel):
    """Запрос на поиск населённых пунктов."""
    CityName: str
    Limit: int = 50
    Page: int = 1


class SearchSettlementsItem(BaseModel):
    """Элемент результата поиска населённых пунктов."""
    Present: str
    Warehouses: str
    MainDescription: str
    Area: str
    Region: str
    SettlementTypeCode: str
    Ref: str
    DeliveryCity: str


class SearchSettlementsResponse(BaseModel):
    """Ответ на поиск населённых пунктов."""
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementsItem] = []


class SearchSettlementStreetsRequest(BaseModel):
    """Запрос на поиск улиц в населенном пункте."""
    SettlementRef: str
    StreetName: str
    Limit: int = 50


class SearchSettlementStreetsItem(BaseModel):
    """Элемент результата поиска улиц."""
    SettlementRef: str
    SettlementStreetRef: str
    SettlementStreetDescription: str
    Present: str
    StreetsType: str
    StreetsTypeDescription: str


class SearchSettlementStreetsResponse(BaseModel):
    """Ответ на поиск улиц в населенном пункте."""
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementStreetsItem] = []