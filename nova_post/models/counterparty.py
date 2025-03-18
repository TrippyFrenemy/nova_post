from typing import Optional, Literal

from pydantic import BaseModel


class CounterpartyRequest(BaseModel):
    """
    Запит на створення або оновлення контрагента.

    Атрибути:
    - `FirstName` (Optional[str]): Ім'я контактної особи (для фізичних осіб).
    - `MiddleName` (Optional[str]): По батькові контактної особи.
    - `LastName` (Optional[str]): Прізвище контактної особи.
    - `Phone` (Optional[str]): Контактний телефон.
    - `Email` (Optional[str]): Адреса електронної пошти.
    - `EDRPOU` (Optional[str]): Код ЄДРПОУ (для юридичних осіб).
    - `CityRef` (Optional[str]): Ідентифікатор міста контрагента.
    - `CounterpartyType` (str): Тип контрагента (`PrivatePerson`, `ThirdPerson`, `Organization`).
    - `CounterpartyProperty` (str): Властивість контрагента (`Recipient`, `Sender`, `ThirdPerson`).
    """
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    EDRPOU: Optional[str] = None
    CityRef: Optional[str] = None
    CounterpartyType: Literal["PrivatePerson", "ThirdPerson", "Organization"]
    CounterpartyProperty: Literal["Sender", "Recipient", "ThirdPerson"]


class CounterpartyResponse(BaseModel):
    """
    Відповідь після створення або оновлення контрагента.

    Атрибути:
    - `Ref` (Optional[str]): Унікальний ідентифікатор контрагента.
    - `Description` (Optional[str]): Опис контрагента.
    - `FirstName` (Optional[str]): Ім'я контактної особи.
    - `MiddleName` (Optional[str]): По батькові контактної особи.
    - `LastName` (Optional[str]): Прізвище контактної особи.
    - `Phone` (Optional[str]): Контактний телефон.
    - `EDRPOU` (Optional[str]): Код ЄДРПОУ (для юридичних осіб).
    - `Counterparty` (Optional[str]): Ідентифікатор контрагента.
    - `OwnershipForm` (Optional[str]): Ідентифікатор форми власності.
    - `OwnershipFormDescription` (Optional[str]): Опис форми власності.
    - `CounterpartyType` (Optional[str]): Тип контрагента.
    """
    Ref: Optional[str] = None
    Description: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None
    EDRPOU: Optional[str] = None
    Counterparty: Optional[str] = None
    OwnershipForm: Optional[str] = None
    OwnershipFormDescription: Optional[str] = None
    CounterpartyType: Optional[Literal["PrivatePerson", "ThirdPerson", "Organization"]] = None


class CounterpartyOptionsRequest(BaseModel):
    """
    Запит на отримання опцій контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контрагента.
    """
    Ref: str


class CounterpartyOptionsResponse(BaseModel):
    """
    Відповідь після отримання опцій контрагента.

    Атрибути:
    - `AddressDocumentDelivery` (Optional[bool]): Чи доступна адресна доставка документів.
    - `AfterpaymentType` (Optional[bool]): Чи доступна післяплата.
    """
    AddressDocumentDelivery: Optional[bool]
    AfterpaymentType: Optional[bool]


class CounterpartyAddressRequest(BaseModel):
    """
    Запит на отримання списку адрес контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контрагента.
    - `CounterpartyProperty` (str): Властивість контрагента (`Recipient`, `Sender`, `ThirdPerson`).
    """
    Ref: str
    CounterpartyProperty: Literal["Sender", "Recipient", "ThirdPerson"]


class CounterpartyAddressResponse(BaseModel):
    """
    Відповідь після отримання списку адрес контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор адреси.
    - `Description` (str): Опис адреси.
    """
    Ref: str
    Description: str


class GetCounterpartiesRequest(BaseModel):
    """
    Запит на отримання списку контрагентів.

    Атрибути:
    - `CounterpartyProperty` (str): Властивість контрагента (`Recipient`, `Sender`, `ThirdPerson`).
    - `Page` (Optional[int]): Номер сторінки (до 100 записів на сторінку).
    - `FindByString` (Optional[str]): Пошуковий рядок для фільтрації контрагентів.
    """
    CounterpartyProperty: Literal["Sender", "Recipient", "ThirdPerson"]
    Page: Optional[int] = None
    FindByString: Optional[str] = None


class GetCounterpartiesResponse(BaseModel):
    """
    Відповідь після отримання списку контрагентів.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контрагента.
    - `Description` (str): Опис контрагента.
    - `City` (Optional[str]): Місто контрагента.
    - `Counterparty` (Optional[str]): Ідентифікатор контрагента.
    - `FirstName` (Optional[str]): Ім'я контактної особи.
    - `LastName` (Optional[str]): Прізвище контактної особи.
    - `MiddleName` (Optional[str]): По батькові контактної особи.
    - `OwnershipFormRef` (Optional[str]): Ідентифікатор форми власності.
    - `OwnershipFormDescription` (Optional[str]): Опис форми власності.
    - `EDRPOU` (Optional[str]): Код ЄДРПОУ (для юридичних осіб).
    - `CounterpartyType` (Optional[str]): Тип контрагента.
    """
    Ref: str
    Description: str
    City: Optional[str]
    Counterparty: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    MiddleName: Optional[str]
    OwnershipFormRef: Optional[str]
    OwnershipFormDescription: Optional[str]
    EDRPOU: Optional[str]
    CounterpartyType: Optional[Literal["PrivatePerson", "ThirdPerson", "Organization"]]


class DeleteCounterpartiesRequest(BaseModel):
    """
    Запит на видалення контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контрагента.
    """
    Ref: str
