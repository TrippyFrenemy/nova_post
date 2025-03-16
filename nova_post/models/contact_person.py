from pydantic import BaseModel
from typing import Optional


class ContactPersonRequest(BaseModel):
    """
    Модель данных для создания/обновления контактного лица.
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
    Модель ответа при работе с контактными лицами.
    """
    Ref: str
    Description: Optional[str] = None
    LastName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    Phones: Optional[str] = None
    Email: Optional[str] = None
