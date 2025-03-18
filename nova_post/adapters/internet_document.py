from typing import List

from ..models.internet_document import (
    DocumentPriceRequest, DocumentPriceResponse,
    DocumentDeliveryDateRequest, DocumentDeliveryDateResponse,
    SaveInternetDocumentRequest, SaveInternetDocumentResponse,
    UpdateInternetDocumentRequest, UpdateInternetDocumentResponse,
    DocumentListRequest, DocumentListResponse,
    DeleteInternetDocumentRequest, DeleteInternetDocumentResponse,
    GenerateReportRequest, GenerateReportResponse,
    EWTemplateListRequest, EWTemplateListResponse
)


class Internet_document:
    """
    Адаптер для роботи з експрес-накладними
    """

    def __init__(self, api):
        self.api = api

    def get_document_price(self, data: DocumentPriceRequest) -> DocumentPriceResponse:
        """
        Розрахунок вартості доставки.

        :param data: Pydantic-модель `GetDocumentPriceRequest`, що містить параметри відправлення.
        :return: Об'єкт `DocumentPriceResponse` із розрахованою вартістю доставки.
        """
        result = self.api.send_request("InternetDocument", "getDocumentPrice", data.model_dump(exclude_unset=True))
        return DocumentPriceResponse.model_validate(result[0])

    def get_document_delivery_date(self, data: DocumentDeliveryDateRequest) -> DocumentDeliveryDateResponse:
        """
        Отримання прогнозованої дати доставки.

        :param data: Pydantic-модель `GetDocumentDeliveryDateRequest`, що містить дані про відправлення.
        :return: Об'єкт `DocumentDeliveryDateResponse` з орієнтовною датою доставки.
        """
        result = self.api.send_request("InternetDocument", "getDocumentDeliveryDate",
                                       data.model_dump(exclude_unset=True))
        return DocumentDeliveryDateResponse.model_validate(result[0])

    def save_internet_document(self, data: SaveInternetDocumentRequest) -> SaveInternetDocumentResponse:
        """
        Створення експрес-накладної.

        :param data: Pydantic-модель `SaveInternetDocumentRequest`, що містить інформацію про вантаж.
        :return: Об'єкт `SaveInternetDocumentResponse` із деталями створеної накладної.
        """
        result = self.api.send_request("InternetDocument", "save", data.model_dump(exclude_unset=True))
        return SaveInternetDocumentResponse.model_validate(result[0])

    def update_internet_document(self, data: UpdateInternetDocumentRequest) -> UpdateInternetDocumentResponse:
        """
        Оновлення даних експрес-накладної.

        :param data: Pydantic-модель `UpdateInternetDocumentRequest`, що містить оновлені параметри накладної.
        :return: Об'єкт `UpdateInternetDocumentResponse` із підтвердженням оновлення.
        """
        result = self.api.send_request("InternetDocument", "update", data.model_dump(exclude_unset=True))
        return UpdateInternetDocumentResponse.model_validate(result[0])

    def get_document_list(self, data: DocumentListRequest) -> List[DocumentListResponse]:
        """
        Отримання списку всіх експрес-накладних.

        :param data: Pydantic-модель `GetDocumentListRequest`, що містить параметри фільтрації.
        :return: Список об'єктів `DocumentListResponse` із деталями накладних.
        """
        result = self.api.send_request("InternetDocument", "getDocumentList", data.model_dump(exclude_unset=True))
        return [DocumentListResponse.model_validate(item) for item in result]

    def delete_internet_document(self, data: DeleteInternetDocumentRequest) -> DeleteInternetDocumentResponse:
        """
        Видалення експрес-накладної.

        :param data: Pydantic-модель `DeleteInternetDocumentRequest`, що містить `Ref` накладної для видалення.
        :return: Об'єкт `DeleteInternetDocumentResponse`, що підтверджує успішне видалення.
        """
        result = self.api.send_request("InternetDocument", "delete", data.model_dump(exclude_unset=True))
        return DeleteInternetDocumentResponse.model_validate(result[0])

    def generate_report(self, data: GenerateReportRequest) -> GenerateReportResponse:
        """
        Формування звіту за накладними.

        :param data: Pydantic-модель `GenerateReportRequest`, що містить параметри звіту.
        :return: Об'єкт `GenerateReportResponse` із згенерованим звітом.
        """
        result = self.api.send_request("InternetDocument", "generateReport", data.model_dump(exclude_unset=True))
        return GenerateReportResponse.model_validate(result[0])

    def get_ew_template_list(self, data: EWTemplateListRequest) -> List[EWTemplateListResponse]:
        """
        Отримання списку документів у заявці на виклик кур’єра.

        :param data: Pydantic-модель `GetEWTemplateListRequest`, що містить параметри запиту.
        :return: Список об'єктів `EWTemplateListResponse` із деталями документів.
        """
        result = self.api.send_request("InternetDocument", "getEWTemplateList", data.model_dump(exclude_unset=True))
        return [EWTemplateListResponse.model_validate(item) for item in result]
