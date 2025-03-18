from typing import Optional

from pydantic import BaseModel


class GetContactPersonRequest(BaseModel):
    """
    Запит на отримання списку контактних осіб контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контрагента.
    - `Page` (Optional[int]): Номер сторінки для пагінації (до 100 записів на сторінку).
    """
    Ref: str
    Page: Optional[int] = None


class DeleteContactPersonRequest(BaseModel):
    """
    Запит на видалення контактної особи контрагента.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контактної особи.
    """
    Ref: str


class ContactPersonRequest(BaseModel):
    """
    Запит на створення або оновлення контактної особи контрагента.

    Атрибути:
    - `CounterpartyRef` (Optional[str]): Ідентифікатор контрагента.
    - `Ref` (Optional[str]): Ідентифікатор контактної особи (вказується для оновлення).
    - `FirstName` (Optional[str]): Ім'я контактної особи.
    - `LastName` (Optional[str]): Прізвище контактної особи.
    - `MiddleName` (Optional[str]): По батькові контактної особи.
    - `Phone` (Optional[str]): Контактний телефон.
    - `Email` (Optional[str]): Адреса електронної пошти.
    """
    CounterpartyRef: Optional[str] = None
    Ref: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    MiddleName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None


class ContactPersonResponse(BaseModel):
    """
    Відповідь після створення, оновлення або отримання контактної особи.

    Атрибути:
    - `Ref` (str): Унікальний ідентифікатор контактної особи.
    - `Description` (Optional[str]): Опис контактної особи.
    - `LastName` (Optional[str]): Прізвище контактної особи.
    - `FirstName` (Optional[str]): Ім'я контактної особи.
    - `MiddleName` (Optional[str]): По батькові контактної особи.
    - `Phones` (Optional[str]): Контактний телефон (може містити декілька номерів).
    - `Email` (Optional[str]): Адреса електронної пошти.
    """
    Ref: str
    Description: Optional[str] = None
    LastName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    Phones: Optional[str] = None
    Email: Optional[str] = None
