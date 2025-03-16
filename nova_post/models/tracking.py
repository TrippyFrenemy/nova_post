from typing import Optional

from pydantic import BaseModel


class TrackingRequest(BaseModel):
    DocumentNumber: str
    Phone: Optional[str] = None


class TrackingResponse(BaseModel):
    Number: str
    Status: str
    WarehouseRecipient: Optional[str] = None
    WarehouseSender: Optional[str] = None
    CityRecipient: Optional[str] = None
    CitySender: Optional[str] = None
    RecipientDateTime: Optional[str] = None
    Phone: Optional[str] = None
