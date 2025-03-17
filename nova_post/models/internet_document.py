from typing import List, Optional
from pydantic import BaseModel


class GetDocumentPriceRequest(BaseModel):
    CitySender: str
    CityRecipient: str
    Weight: float
    ServiceType: str
    Cost: Optional[int] = 300
    CargoType: str
    SeatsAmount: int
    RedeliveryCalculate: Optional[dict] = None
    PackCount: Optional[int] = None
    PackRef: Optional[str] = None
    Amount: Optional[int] = None
    CargoDetails: Optional[List[dict]] = None
    CargoDescription: Optional[str] = None


class DocumentPriceResponse(BaseModel):
    AssessedCost: int
    Cost: int
    CostRedelivery: Optional[str] = None
    TZoneInfo: Optional[dict] = None
    CostPack: Optional[str] = None


class GetDocumentDeliveryDateRequest(BaseModel):
    DateTime: Optional[str] = None
    ServiceType: str
    CitySender: str
    CityRecipient: str


class DocumentDeliveryDateResponse(BaseModel):
    DeliveryDate: dict


class SaveInternetDocumentRequest(BaseModel):
    PayerType: str
    PaymentMethod: str
    DateTime: str
    CargoType: str
    Weight: float
    ServiceType: str
    SeatsAmount: int
    Description: str
    Cost: int
    CitySender: str
    Sender: str
    SenderAddress: str
    ContactSender: str
    SendersPhone: str
    CityRecipient: str
    Recipient: str
    RecipientAddress: str
    ContactRecipient: str
    RecipientsPhone: str
    OptionsSeat: Optional[List[dict]] = None
    BackwardDeliveryData: Optional[List[dict]] = None


class SaveInternetDocumentResponse(BaseModel):
    Ref: str
    CostOnSite: int
    EstimatedDeliveryDate: str
    IntDocNumber: str
    TypeDocument: str


class GetDocumentListRequest(BaseModel):
    DateTimeFrom: str
    DateTimeTo: str
    Page: Optional[int] = 1
    GetFullList: Optional[int] = 0


class DocumentListResponse(BaseModel):
    Ref: str
    DateTime: str
    IntDocNumber: str
    Cost: str
    CitySender: str
    CityRecipient: str
    PayerType: str
    StateId: int
    StateName: str


class DeleteInternetDocumentRequest(BaseModel):
    DocumentRefs: List[str] = None


class DeleteInternetDocumentResponse(BaseModel):
    Ref: str


class GenerateReportRequest(BaseModel):
    DocumentRefs: List[str] = None
    Type: str  # 'xls' або 'csv'
    DateTime: str


class GenerateReportResponse(BaseModel):
    Ref: str
    DateTime: str
    Weight: str
    CostOnSite: str
    PayerType: str
    PaymentMethod: str
    IntDocNumber: str


class GetEWTemplateListRequest(BaseModel):
    Page: int
    Limit: int
    PickupNumber: str
    State: Optional[str] = None


class EWTemplateListResponse(BaseModel):
    EWNumber: str
    StateId: str
    RecipientCityRef: str
    RecipientAddress: str
    Cost: str
    IntDocNumber: str


class UpdateInternetDocumentRequest(BaseModel):
    Ref: str
    PayerType: str
    PaymentMethod: str
    DateTime: str
    CargoType: str
    Weight: float
    ServiceType: str
    SeatsAmount: int
    Description: str
    Cost: int
    CitySender: str
    Sender: str
    SenderAddress: str
    ContactSender: str
    SendersPhone: str
    CityRecipient: str
    Recipient: str
    RecipientAddress: str
    ContactRecipient: str
    RecipientsPhone: str
    OptionsSeat: Optional[List[dict]] = None
    BackwardDeliveryData: Optional[List[dict]] = None


class UpdateInternetDocumentResponse(BaseModel):
    Ref: str
    CostOnSite: str
    EstimatedDeliveryDate: str
    IntDocNumber: str
    TypeDocument: str
