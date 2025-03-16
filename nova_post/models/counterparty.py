from typing import Optional

from pydantic import BaseModel


class CounterpartyRequest(BaseModel):
    """
    Модель для передачи полей в запросах на создание/обновление контрагента.
    Может меняться в зависимости от того, какой именно контрагент создаётся (PrivatePerson, ThirdPerson, Organization).
    """
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    EDRPOU: Optional[str] = None
    CityRef: Optional[str] = None
    CounterpartyType: str
    CounterpartyProperty: str  # Recipient, Sender, ThirdPerson, etc.


class CounterpartyResponse(BaseModel):
    """
    Модель, описывающая поля, которые возвращает API при создании/обновлении/получении контрагентов.
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
    CounterpartyType: Optional[str] = None


class CounterpartyOptions(BaseModel):
    """
    Модель опций контрагента (полей может быть много, см. Counterparty_instructions.txt).
    Пример минимального набора.
    """
    AddressDocumentDelivery: Optional[bool]
    AfterpaymentType: Optional[bool]
    # ... И т.д., остальные поля по необходимости


class CounterpartyAddress(BaseModel):
    """
    Модель адреса контрагента
    """
    Ref: str
    Description: str


class GetCounterpartiesResponse(BaseModel):
    """
    Модель для списка контрагентов (метод getCounterparties).
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
    CounterpartyType: Optional[str]
