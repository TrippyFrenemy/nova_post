from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class TimeIntervalRequest(BaseModel):
    """
    Запит на отримання списку часових інтервалів для міста.

    Атрибути:
    - `RecipientCityRef` (str): Ідентифікатор міста для якого запитується список інтервалів.
    - `DateTime` (Optional[str]): Дата у форматі "dd.mm.YYYY" (необов'язковий, за замовчуванням поточна дата).
    """
    RecipientCityRef: str
    DateTime: Optional[str] = None

    @field_validator("DateTime", mode="before")
    def set_default_date(cls, value):
        today = datetime.now().strftime("%d.%m.%Y")
        if not value:
            return today
        try:
            input_date = datetime.strptime(value, "%d.%m.%Y").strftime("%d.%m.%Y")
            return max(input_date, today)
        except ValueError:
            return today


class TimeIntervalResponse(BaseModel):
    """
    Відповідь із часовими інтервалами.

    Атрибути:
    - `Number` (str): Унікальний ідентифікатор інтервалу.
    - `Start` (str): Час початку інтервалу.
    - `End` (str): Час завершення інтервалу.
    """
    Number: str
    Start: str
    End: str


class CargoTypeResponse(BaseModel):
    """
    Відповідь із типами вантажу.

    Атрибути:
    - `Ref` (str): Ідентифікатор типу вантажу.
    - `Description` (str): Опис типу вантажу.
    """
    Ref: str
    Description: str


class PalletResponse(BaseModel):
    """
    Відповідь із видами палет.

    Атрибути:
    - `Ref` (str): Ідентифікатор палети.
    - `Description` (str): Опис палети українською мовою.
    - `DescriptionRu` (Optional[str]): Опис палети російською мовою (необов'язковий).
    - `Weight` (str): Вага палети.
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Weight: str


class PayerForRedeliveryResponse(BaseModel):
    """
    Відповідь із типами платників зворотної доставки.

    Атрибути:
    - `Ref` (str): Ідентифікатор платника.
    - `Description` (str): Опис платника.
    """
    Ref: str
    Description: str


class PackListResponse(BaseModel):
    """
    Відповідь із видами упаковки.

    Атрибути:
    - `Ref` (str): Ідентифікатор упаковки.
    - `Description` (str): Опис упаковки українською мовою.
    - `DescriptionRu` (Optional[str]): Опис упаковки російською мовою (необов'язковий).
    - `Length` (str): Довжина упаковки.
    - `Width` (str): Ширина упаковки.
    - `Height` (str): Висота упаковки.
    - `VolumetricWeight` (str): Об'ємна вага упаковки.
    - `TypeOfPacking` (Optional[str]): Тип упаковки (необов'язковий).
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Length: str
    Width: str
    Height: str
    VolumetricWeight: str
    TypeOfPacking: Optional[str] = None


class TiresWheelsResponse(BaseModel):
    """
    Відповідь із доступними шинами та дисками.

    Атрибути:
    - `Ref` (str): Ідентифікатор товару.
    - `Description` (str): Опис українською мовою.
    - `DescriptionRu` (Optional[str]): Опис російською мовою (необов'язковий).
    - `Weight` (str): Вага товару.
    - `DescriptionType` (str): Тип позиції (Tires або Wheels).
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Weight: str
    DescriptionType: str


class CargoDescriptionResponse(BaseModel):
    """
    Відповідь із можливими описами вантажів.

    Атрибути:
    - `Ref` (str): Ідентифікатор опису.
    - `Description` (str): Опис вантажу українською мовою.
    - `DescriptionRu` (Optional[str]): Опис вантажу російською мовою (необов'язковий).
    """
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None


class ServiceTypeResponse(BaseModel):
    """
    Відповідь із видами технологій доставки.

    Атрибути:
    - `Ref` (str): Ідентифікатор технології доставки.
    - `Description` (str): Опис технології доставки.
    """
    Ref: str
    Description: str


class OwnershipFormResponse(BaseModel):
    """
    Відповідь із формами власності.

    Атрибути:
    - `Ref` (str): Ідентифікатор форми власності.
    - `Description` (str): Назва форми власності.
    """
    Ref: str
    Description: str
