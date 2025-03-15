from pydantic import BaseModel


class ParcelStatus(BaseModel):
    Number: str
    Status: str
    WarehouseRecipient: str
    WarehouseSender: str | None = None
    CityRecipient: str | None = None
    CitySender: str | None = None
    RecipientDateTime: str | None = None
