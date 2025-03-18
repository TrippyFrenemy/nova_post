from typing import Optional

from pydantic import BaseModel


class TrackingRequest(BaseModel):
    """
    Запит на відстеження посилки.

    Атрибути:
    - `DocumentNumber` (str): Номер експрес-накладної для відстеження.
    - `Phone` (Optional[str]): Номер телефону одержувача або відправника (необов’язково).
    """
    DocumentNumber: str
    Phone: Optional[str] = None


class TrackingResponse(BaseModel):
    """
    Відповідь із результатами відстеження посилки.

    Атрибути:
    - `Number` (str): Номер експрес-накладної.
    - `Status` (str): Поточний статус відправлення.
    - `WarehouseRecipient` (Optional[str]): Відділення отримувача (необов’язково).
    - `WarehouseSender` (Optional[str]): Відділення відправника (необов’язково).
    - `CityRecipient` (Optional[str]): Місто отримувача (необов’язково).
    - `CitySender` (Optional[str]): Місто відправника (необов’язково).
    - `RecipientDateTime` (Optional[str]): Дата отримання посилки (необов’язково).
    - `Phone` (Optional[str]): Контактний номер телефону (необов’язково).
    """
    Number: str
    Status: str
    WarehouseRecipient: Optional[str] = None
    WarehouseSender: Optional[str] = None
    CityRecipient: Optional[str] = None
    CitySender: Optional[str] = None
    RecipientDateTime: Optional[str] = None
    Phone: Optional[str] = None
