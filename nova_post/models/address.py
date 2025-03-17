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


class SearchSettlementsRequest(BaseModel):
    CityName: str
    Limit: int = 50
    Page: int = 1


class SearchSettlementsItem(BaseModel):
    Present: str
    Warehouses: str
    MainDescription: str
    Area: str
    Region: str
    SettlementTypeCode: str
    Ref: str
    DeliveryCity: str


class SearchSettlementsResponse(BaseModel):
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementsItem] = []


class SearchSettlementStreetsRequest(BaseModel):
    SettlementRef: str
    StreetName: str
    Limit: int = 50


class SearchSettlementStreetsItem(BaseModel):
    SettlementRef: str
    SettlementStreetRef: str
    SettlementStreetDescription: str
    Present: str
    StreetsType: str
    StreetsTypeDescription: str


class SearchSettlementStreetsResponse(BaseModel):
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementStreetsItem] = []
