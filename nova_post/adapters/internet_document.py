from typing import List
from ..models.internet_document import (
    GetDocumentPriceRequest, DocumentPriceResponse,
    GetDocumentDeliveryDateRequest, DocumentDeliveryDateResponse,
    SaveInternetDocumentRequest, SaveInternetDocumentResponse,
    UpdateInternetDocumentRequest, UpdateInternetDocumentResponse,
    GetDocumentListRequest, DocumentListResponse,
    DeleteInternetDocumentRequest, DeleteInternetDocumentResponse,
    GenerateReportRequest, GenerateReportResponse,
    GetEWTemplateListRequest, EWTemplateListResponse
)


class Internet_document:
    """Класс для работы с экспресс-накладными (ЕН) в API Новой Почты."""

    def __init__(self, api):
        self.api = api

    def get_document_price(self, data: GetDocumentPriceRequest) -> DocumentPriceResponse:
        """Рассчитать стоимость доставки."""
        result = self.api.send_request("InternetDocument", "getDocumentPrice", data.model_dump(exclude_unset=True))
        return DocumentPriceResponse.model_validate(result[0])

    def get_document_delivery_date(self, data: GetDocumentDeliveryDateRequest) -> DocumentDeliveryDateResponse:
        """Получить прогнозируемую дату доставки."""
        result = self.api.send_request("InternetDocument", "getDocumentDeliveryDate", data.model_dump(exclude_unset=True))
        return DocumentDeliveryDateResponse.model_validate(result[0])

    def save_internet_document(self, data: SaveInternetDocumentRequest) -> SaveInternetDocumentResponse:
        """Создать новую экспресс-накладную."""
        result = self.api.send_request("InternetDocument", "save", data.model_dump(exclude_unset=True))
        return SaveInternetDocumentResponse.model_validate(result[0])

    def update_internet_document(self, data: UpdateInternetDocumentRequest) -> UpdateInternetDocumentResponse:
        """Обновить данные экспресс-накладной."""
        result = self.api.send_request("InternetDocument", "update", data.model_dump(exclude_unset=True))
        return UpdateInternetDocumentResponse.model_validate(result[0])

    def get_document_list(self, data: GetDocumentListRequest) -> List[DocumentListResponse]:
        """Получить список всех экспресс-накладных."""
        result = self.api.send_request("InternetDocument", "getDocumentList", data.model_dump(exclude_unset=True))
        return [DocumentListResponse.model_validate(item) for item in result]

    def delete_internet_document(self, data: DeleteInternetDocumentRequest) -> DeleteInternetDocumentResponse:
        """Удалить экспресс-накладную."""
        result = self.api.send_request("InternetDocument", "delete", data.model_dump(exclude_unset=True))
        return DeleteInternetDocumentResponse.model_validate(result[0])

    def generate_report(self, data: GenerateReportRequest) -> GenerateReportResponse:
        """Сформировать отчет по накладным."""
        result = self.api.send_request("InternetDocument", "generateReport", data.model_dump(exclude_unset=True))
        return GenerateReportResponse.model_validate(result[0])

    def get_ew_template_list(self, data: GetEWTemplateListRequest) -> List[EWTemplateListResponse]:
        """Получить список документов в заявке на вызов курьера."""
        result = self.api.send_request("InternetDocument", "getEWTemplateList", data.model_dump(exclude_unset=True))
        return [EWTemplateListResponse.model_validate(item) for item in result]
