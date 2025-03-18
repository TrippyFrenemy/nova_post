from typing import Optional, List

from pydantic import BaseModel


class City(BaseModel):
    """
    Модель міста.

    Атрибути:
    - `Ref` (str): Ідентифікатор міста.
    - `Description` (str): Назва міста українською мовою.
    - `DescriptionRu` (Optional[str]): Назва міста російською мовою (необов'язковий).
    - `Area` (Optional[str]): Ідентифікатор області (необов'язковий).
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Area: Optional[str] = None


class Warehouse(BaseModel):
    """
    Модель відділення.

    Атрибути:
    - `SiteKey` (int): Унікальний ключ відділення.
    - `Description` (str): Назва відділення українською мовою.
    - `DescriptionRu` (Optional[str]): Назва відділення російською мовою (необов'язковий).
    - `Number` (str): Номер відділення.
    - `CityRef` (str): Ідентифікатор міста, в якому знаходиться відділення.
    - `TypeOfWarehouse` (Optional[str]): Тип відділення (необов'язковий).
    """
    SiteKey: int
    Description: str
    DescriptionRu: Optional[str] = None
    Number: str
    CityRef: str
    TypeOfWarehouse: Optional[str] = None


class Street(BaseModel):
    """
    Модель вулиці.

    Атрибути:
    - `Ref` (str): Ідентифікатор вулиці.
    - `Description` (str): Назва вулиці.
    - `StreetsTypeRef` (str): Ідентифікатор типу вулиці.
    - `StreetsType` (str): Опис типу вулиці.
    """
    Ref: str
    Description: str
    StreetsTypeRef: str
    StreetsType: str


class Area(BaseModel):
    """
    Модель області.

    Атрибути:
    - `Ref` (str): Ідентифікатор області.
    - `Description` (str): Назва області українською мовою.
    - `DescriptionRu` (Optional[str]): Назва області російською мовою (необов'язковий).
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None


class Settlement(BaseModel):
    """
    Модель населеного пункту.

    Атрибути:
    - `Ref` (str): Ідентифікатор населеного пункту.
    - `Description` (str): Назва населеного пункту українською мовою.
    - `DescriptionRu` (Optional[str]): Назва населеного пункту російською мовою (необов'язковий).
    - `AreaRef` (str): Ідентифікатор області, до якої належить населений пункт.
    - `Type` (str): Тип населеного пункту.
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    AreaRef: str
    Type: str


class AddressSaveRequest(BaseModel):
    """
    Модель для створення адреси.

    Атрибути:
    - `CounterpartyRef` (str): Ідентифікатор контрагента.
    - `StreetRef` (str): Ідентифікатор вулиці.
    - `BuildingNumber` (str): Номер будинку.
    - `Flat` (Optional[str]): Номер квартири (необов'язковий).
    - `Note` (Optional[str]): Додаткові примітки (необов'язковий).
    """
    CounterpartyRef: str
    StreetRef: str
    BuildingNumber: str
    Flat: Optional[str] = None
    Note: Optional[str] = None


class AddressUpdateRequest(BaseModel):
    """
    Модель для оновлення адреси.

    Атрибути:
    - `Ref` (str): Ідентифікатор адреси.
    - `CounterpartyRef` (Optional[str]): Ідентифікатор контрагента (необов'язковий).
    - `StreetRef` (Optional[str]): Ідентифікатор вулиці (необов'язковий).
    - `BuildingNumber` (Optional[str]): Номер будинку (необов'язковий).
    - `Flat` (Optional[str]): Номер квартири (необов'язковий).
    - `Note` (Optional[str]): Додаткові примітки (необов'язковий).
    """
    Ref: str
    CounterpartyRef: Optional[str] = None
    StreetRef: Optional[str] = None
    BuildingNumber: Optional[str] = None
    Flat: Optional[str] = None
    Note: Optional[str] = None


class AddressDeleteRequest(BaseModel):
    """
    Модель для видалення адреси.

    Атрибути:
    - `Ref` (str): Ідентифікатор адреси.
    """
    Ref: str


class AddressResponse(BaseModel):
    """
    Відповідь при створенні, оновленні або видаленні адреси.

    Атрибути:
    - `Ref` (str): Ідентифікатор адреси.
    - `Description` (Optional[str]): Опис адреси (необов'язковий).
    """
    Ref: str
    Description: Optional[str] = None


class GetCitiesRequest(BaseModel):
    """
    Модель запиту на отримання списку міст.

    Атрибути:
    - `FindByString` (Optional[str]): Пошук міста за назвою (необов'язковий).
    - `Ref` (Optional[str]): Ідентифікатор міста (необов'язковий).
    - `Limit` (Optional[int]): Ліміт результатів (необов'язковий).
    - `Page` (Optional[int]): Номер сторінки (необов'язковий).
    - `Warehouse` (Optional[str]): Фільтр за наявністю відділень (необов'язковий).
    """
    FindByString: Optional[str] = None
    Ref: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None
    Warehouse: Optional[str] = None


class GetWarehousesRequest(BaseModel):
    """
    Модель запиту на отримання списку відділень.

    Атрибути:
    - `CityRef` (Optional[str]): Ідентифікатор міста (необов'язковий).
    - `WarehouseRef` (Optional[str]): Ідентифікатор відділення (необов'язковий).
    - `Limit` (Optional[int]): Ліміт результатів (необов'язковий).
    - `Page` (Optional[int]): Номер сторінки (необов'язковий).
    - `FindByString` (Optional[str]): Пошук відділення за назвою (необов'язковий).
    """
    CityRef: Optional[str] = None
    WarehouseRef: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None
    FindByString: Optional[str] = None


class GetStreetsRequest(BaseModel):
    """
    Модель запиту на отримання списку вулиць.

    Атрибути:
    - `CityRef` (str): Ідентифікатор міста.
    - `FindByString` (Optional[str]): Пошук вулиці за назвою (необов'язковий).
    - `Ref` (Optional[str]): Ідентифікатор вулиці (необов'язковий).
    - `Limit` (Optional[int]): Ліміт результатів (необов'язковий).
    - `Page` (Optional[int]): Номер сторінки (необов'язковий).
    """
    CityRef: str
    FindByString: Optional[str] = None
    Ref: Optional[str] = None
    Limit: Optional[int] = None
    Page: Optional[int] = None


class SearchSettlementsRequest(BaseModel):
    """
    Запит на пошук населених пунктів.

    Атрибути:
    - `CityName` (str): Назва населеного пункту.
    - `Limit` (int): Кількість записів на сторінці (за замовчуванням 50).
    - `Page` (int): Номер сторінки (за замовчуванням 1).
    """
    CityName: str
    Limit: int = 50
    Page: int = 1


class SearchSettlementsItem(BaseModel):
    """
    Елемент результату пошуку населених пунктів.

    Атрибути:
    - `Present` (str): Повна назва населеного пункту.
    - `Warehouses` (str): Кількість відділень у населеному пункті.
    - `MainDescription` (str): Основний опис населеного пункту.
    - `Area` (str): Область, до якої належить населений пункт.
    - `Region` (str): Район населеного пункту.
    - `SettlementTypeCode` (str): Код типу населеного пункту.
    - `Ref` (str): Ідентифікатор населеного пункту.
    - `DeliveryCity` (str): Ідентифікатор міста доставки.
    """
    Present: str
    Warehouses: str
    MainDescription: str
    Area: str
    Region: str
    SettlementTypeCode: str
    Ref: str
    DeliveryCity: str


class SearchSettlementsResponse(BaseModel):
    """
    Відповідь на пошук населених пунктів.

    Атрибути:
    - `TotalCount` (Optional[str]): Загальна кількість знайдених об'єктів.
    - `Addresses` (List[SearchSettlementsItem]): Список знайдених населених пунктів.
    """
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementsItem] = []


class SearchSettlementStreetsRequest(BaseModel):
    """
    Запит на пошук вулиць у населеному пункті.

    Атрибути:
    - `SettlementRef` (str): Ідентифікатор населеного пункту.
    - `StreetName` (str): Назва вулиці.
    - `Limit` (int): Кількість записів (за замовчуванням 50).
    """
    SettlementRef: str
    StreetName: str
    Limit: int = 50


class SearchSettlementStreetsItem(BaseModel):
    """
    Елемент результату пошуку вулиць.

    Атрибути:
    - `SettlementRef` (str): Ідентифікатор населеного пункту.
    - `SettlementStreetRef` (str): Ідентифікатор вулиці.
    - `SettlementStreetDescription` (str): Назва вулиці.
    - `Present` (str): Повна назва вулиці, що включає тип вулиці та її назву.
    - `StreetsType` (str): Ідентифікатор типу вулиці (наприклад, вулиця, проспект тощо).
    - `StreetsTypeDescription` (str): Опис типу вулиці.
    """
    SettlementRef: str
    SettlementStreetRef: str
    SettlementStreetDescription: str
    Present: str
    StreetsType: str
    StreetsTypeDescription: str


class SearchSettlementStreetsResponse(BaseModel):
    """
    Відповідь на пошук вулиць у населеному пункті.

    Атрибути:
    - `TotalCount` (Optional[str]): Загальна кількість знайдених об'єктів.
    - `Addresses` (List[SearchSettlementStreetsItem]): Список знайдених вулиць.
    """
    TotalCount: Optional[str] = None
    Addresses: List[SearchSettlementStreetsItem] = []
