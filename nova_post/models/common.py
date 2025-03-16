from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class TimeIntervalRequest(BaseModel):
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
    Number: str
    Start: str
    End: str


class CargoTypeResponse(BaseModel):
    Ref: str
    Description: str


class PalletResponse(BaseModel):
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Weight: str


class PayerForRedeliveryResponse(BaseModel):
    Ref: str
    Description: str


class PackListResponse(BaseModel):
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Length: str
    Width: str
    Height: str
    VolumetricWeight: str
    TypeOfPacking: Optional[str] = None


class TiresWheelsResponse(BaseModel):
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Weight: str
    DescriptionType: str


class CargoDescriptionResponse(BaseModel):
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None


class ServiceTypeResponse(BaseModel):
    Ref: str
    Description: str


class OwnershipFormResponse(BaseModel):
    Ref: str
    Description: str
