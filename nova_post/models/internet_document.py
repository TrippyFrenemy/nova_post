from datetime import datetime
from typing import List, Optional, Literal

from pydantic import BaseModel, field_validator


class DocumentPriceRequest(BaseModel):
    """
    Запит на розрахунок вартості доставки.

    Атрибути:
    - `CitySender` (str): Ідентифікатор міста відправника.
    - `CityRecipient` (str): Ідентифікатор міста отримувача.
    - `Weight` (float): Фактична вага відправлення.
    - `ServiceType` (str): Тип послуги (наприклад, "WarehouseWarehouse").
    - `Cost` (Optional[int]): Оціночна вартість вантажу (за замовчуванням 300 грн).
    - `CargoType` (str): Тип вантажу (наприклад, "Cargo", "Documents").
    - `SeatsAmount` (int): Кількість місць у відправленні.
    - `RedeliveryCalculate` (Optional[dict]): Параметри зворотної доставки (необов’язково).
    - `PackCount` (Optional[int]): Кількість пакувань (необов’язково).
    - `PackRef` (Optional[str]): Ідентифікатор пакування (необов’язково).
    - `Amount` (Optional[int]): Сума зворотної доставки (необов’язково).
    - `CargoDetails` (Optional[List[dict]]): Деталі вантажу (необов’язково).
    - `CargoDescription` (Optional[str]): Ідентифікатор типу відправлення (необов’язково).
    """
    CitySender: str
    CityRecipient: str
    Weight: float
    ServiceType: str
    Cost: Optional[int] = 300
    CargoType: Literal["Cargo", "Documents", "TiresWheels", "Pallet"]
    SeatsAmount: int
    RedeliveryCalculate: Optional[dict] = None
    PackCount: Optional[int] = None
    PackRef: Optional[str] = None
    Amount: Optional[int] = None
    CargoDetails: Optional[List[dict]] = None
    CargoDescription: Optional[str] = None


class DocumentPriceResponse(BaseModel):
    """
    Відповідь із розрахованою вартістю доставки.

    Атрибути:
    - `AssessedCost` (int): Оціночна вартість вантажу.
    - `Cost` (int): Вартість доставки.
    - `CostRedelivery` (Optional[str]): Вартість зворотної доставки (необов’язково).
    - `TZoneInfo` (Optional[dict]): Інформація про тарифну зону доставки (необов’язково).
    - `CostPack` (Optional[str]): Вартість пакування (необов’язково).
    """
    AssessedCost: int
    Cost: int
    CostRedelivery: Optional[str] = None
    TZoneInfo: Optional[dict] = None
    CostPack: Optional[str] = None


class DocumentDeliveryDateRequest(BaseModel):
    """
    Запит на отримання прогнозованої дати доставки.

    Атрибути:
    - `DateTime` (Optional[str]): Дата створення експрес-накладної (необов’язково).
    - `ServiceType` (str): Тип послуги.
    - `CitySender` (str): Ідентифікатор міста відправника.
    - `CityRecipient` (str): Ідентифікатор міста отримувача.
    """
    DateTime: Optional[str] = None
    ServiceType: str
    CitySender: str
    CityRecipient: str


class DocumentDeliveryDateResponse(BaseModel):
    """
    Відповідь із прогнозованою датою доставки.

    Атрибути:
    - `DeliveryDate` (dict): Орієнтовна дата доставки.
    """
    DeliveryDate: dict


class SaveInternetDocumentRequest(BaseModel):
    """
    Запит на створення експрес-накладної.

    Атрибути:
    - `PayerType` (str): Тип платника (Sender, Recipient, ThirdPerson).
    - `PaymentMethod` (str): Форма розрахунку (Cash/NonCash).
    - `DateTime` (str): Дата відправки у форматі "дд.мм.рррр".
    - `CargoType` (str): Тип вантажу.
    - `Weight` (float): Фактична вага вантажу.
    - `ServiceType` (str): Технологія доставки.
    - `SeatsAmount` (int): Кількість місць відправлення.
    - `Description` (str): Опис вантажу.
    - `Cost` (int): Оціночна вартість вантажу.
    - `CitySender` (str): Ідентифікатор міста відправника.
    - `Sender` (str): Ідентифікатор контрагента-відправника.
    - `SenderAddress` (str): Ідентифікатор адреси відправника.
    - `ContactSender` (str): Ідентифікатор контактної особи відправника.
    - `SendersPhone` (str): Телефон відправника.
    - `CityRecipient` (str): Ідентифікатор міста отримувача.
    - `Recipient` (str): Ідентифікатор контрагента-отримувача.
    - `RecipientAddress` (str): Ідентифікатор адреси отримувача.
    - `ContactRecipient` (str): Ідентифікатор контактної особи отримувача.
    - `RecipientsPhone` (str): Телефон отримувача.
    - `OptionsSeat` (Optional[List[dict]]): Параметри кожного місця (необов’язково).
    - `BackwardDeliveryData` (Optional[List[dict]]): Інформація про зворотну доставку (необов’язково).
    """
    PayerType: Literal["Sender", "Recipient", "ThirdPerson"]
    PaymentMethod: Literal["Cash", "NonCash"]
    DateTime: str
    CargoType: str
    Weight: float
    ServiceType: Literal["DoorsDoors", "DoorsWarehouse", "WarehouseWarehouse", "WarehouseDoors"]
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


class SaveInternetDocumentResponse(BaseModel):
    """
    Відповідь із деталями створеної експрес-накладної.

    Атрибути:
    - `Ref` (str): Ідентифікатор експрес-накладної.
    - `CostOnSite` (int): Вартість доставки.
    - `EstimatedDeliveryDate` (str): Орієнтовна дата доставки.
    - `IntDocNumber` (str): Номер експрес-накладної.
    - `TypeDocument` (str): Тип експрес-накладної.
    """
    Ref: str
    CostOnSite: int
    EstimatedDeliveryDate: str
    IntDocNumber: str
    TypeDocument: str


class DocumentListRequest(BaseModel):
    """
    Запит на отримання списку експрес-накладних.

    Атрибути:
    - `DateTimeFrom` (str): Дата початку періоду пошуку.
    - `DateTimeTo` (str): Дата завершення періоду пошуку.
    - `Page` (Optional[int]): Номер сторінки (за замовчуванням 1).
    - `GetFullList` (Optional[int]): Ознака отримання всього списку (0 – посторінкове завантаження, 1 – весь список).
    """
    DateTimeFrom: str
    DateTimeTo: str
    Page: Optional[int] = 1
    GetFullList: Optional[int] = 0


class DocumentListResponse(BaseModel):
    """
    Відповідь із деталями експрес-накладних.

    Атрибути:
    - `Ref` (str): Ідентифікатор експрес-накладної.
    - `DateTime` (str): Дата створення накладної.
    - `IntDocNumber` (str): Номер експрес-накладної.
    - `Cost` (str): Вартість доставки.
    - `CitySender` (str): Ідентифікатор міста відправника.
    - `CityRecipient` (str): Ідентифікатор міста отримувача.
    - `PayerType` (str): Тип платника.
    - `StateId` (int): Ідентифікатор статусу накладної.
    - `StateName` (str): Опис статусу накладної.
    """
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
    """
    Запит на видалення експрес-накладної.

    Атрибути:
    - `DocumentRefs` (List[str]): Список ідентифікаторів експрес-накладних для видалення.
    """
    DocumentRefs: List[str] = None


class DeleteInternetDocumentResponse(BaseModel):
    """
    Відповідь після видалення експрес-накладної.

    Атрибути:
    - `Ref` (str): Ідентифікатор видаленої експрес-накладної.
    """
    Ref: str


class GenerateReportRequest(BaseModel):
    """
    Запит на створення звіту за накладними.

    Атрибути:
    - `DocumentRefs` (List[str]): Список ідентифікаторів накладних для звіту.
    - `Type` (str): Формат звіту ('xls' або 'csv').
    - `DateTime` (str): Дата формування звіту.
    """
    DocumentRefs: List[str] = None
    Type: str
    DateTime: str


class GenerateReportResponse(BaseModel):
    """
    Відповідь із деталями згенерованого звіту.

    Атрибути:
    - `Ref` (str): Ідентифікатор згенерованого звіту.
    - `DateTime` (str): Дата створення звіту.
    - `Weight` (str): Вага вантажу.
    - `CostOnSite` (str): Вартість доставки.
    - `PayerType` (str): Тип платника.
    - `PaymentMethod` (str): Форма оплати.
    - `IntDocNumber` (str): Номер експрес-накладної.
    """
    Ref: str
    DateTime: str
    Weight: str
    CostOnSite: str
    PayerType: str
    PaymentMethod: str
    IntDocNumber: str


class EWTemplateListRequest(BaseModel):
    """
    Запит на отримання списку документів у заявці на виклик кур’єра.

    Атрибути:
    - `Page` (int): Номер сторінки для пагінації.
    - `Limit` (int): Кількість записів на сторінці.
    - `PickupNumber` (str): Номер заявки на виклик кур’єра.
    - `State` (Optional[str]): Ідентифікатор стану документа (необов’язковий).
    """
    Page: int
    Limit: int
    PickupNumber: str
    State: Optional[str] = None


class EWTemplateListResponse(BaseModel):
    """
    Відповідь із деталями документів у заявці на виклик кур’єра.

    Атрибути:
    - `EWNumber` (str): Номер експрес-накладної.
    - `StateId` (str): Ідентифікатор стану документа.
    - `RecipientCityRef` (str): Ідентифікатор міста отримувача.
    - `RecipientAddress` (str): Ідентифікатор адреси отримувача.
    - `Cost` (str): Вартість доставки.
    - `IntDocNumber` (str): Внутрішній номер експрес-накладної.
    """
    EWNumber: str
    StateId: str
    RecipientCityRef: str
    RecipientAddress: str
    Cost: str
    IntDocNumber: str


class UpdateInternetDocumentRequest(BaseModel):
    """
    Запит на оновлення експрес-накладної.

    Атрибути:
    - `Ref` (str): Ідентифікатор експрес-накладної.
    - `PayerType` (str): Тип платника.
    - `PaymentMethod` (str): Форма розрахунку.
    - `DateTime` (str): Дата відправки.
    - `CargoType` (str): Тип вантажу.
    - `Weight` (float): Вага вантажу.
    - `ServiceType` (str): Тип доставки.
    - `SeatsAmount` (int): Кількість місць.
    - `Description` (str): Опис вантажу.
    - `Cost` (int): Оціночна вартість.
    """
    Ref: str
    PayerType: Literal["Sender", "Recipient", "ThirdPerson"]
    PaymentMethod: Literal["Cash", "NonCash"]
    DateTime: str
    CargoType: str
    Weight: float
    ServiceType: Literal["DoorsDoors", "DoorsWarehouse", "WarehouseWarehouse", "WarehouseDoors"]
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
    """
    Відповідь після оновлення експрес-накладної.

    Атрибути:
    - `Ref` (str): Ідентифікатор експрес-накладної.
    - `CostOnSite` (str): Вартість доставки після оновлення.
    - `EstimatedDeliveryDate` (str): Прогнозована дата доставки.
    - `IntDocNumber` (str): Номер експрес-накладної.
    - `TypeDocument` (str): Тип експрес-накладної.
    """
    Ref: str
    CostOnSite: str
    EstimatedDeliveryDate: str
    IntDocNumber: str
    TypeDocument: str
