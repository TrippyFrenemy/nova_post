from typing import Optional
from pydantic import BaseModel


class ParcelStatus(BaseModel):
    Number: str
    Status: str
    WarehouseRecipient: Optional[str] = None
    WarehouseSender: Optional[str] = None
    CityRecipient: Optional[str] = None
    CitySender: Optional[str] = None
    RecipientDateTime: Optional[str] = None
    Phone: Optional[str] = None
