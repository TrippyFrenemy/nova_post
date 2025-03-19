from unittest.mock import Mock

import pytest

from nova_post.api import NovaPostApi
from nova_post.models.internet_document import (
    DocumentPriceRequest, DocumentDeliveryDateRequest,
    SaveInternetDocumentRequest, DocumentListRequest,
    DeleteInternetDocumentRequest
)


@pytest.fixture
def mock_api():
    api = Mock(spec=NovaPostApi)
    api.internet_document = Mock()
    return api


def test_get_document_price(mock_api):
    mock_response = Mock()
    mock_response.Cost = 150.50
    mock_response.AssessedCost = 500.00
    mock_response.CostRedelivery = 75.25
    mock_api.internet_document.get_document_price.return_value = mock_response

    # Execute test
    request = DocumentPriceRequest(
        CitySender="db5c8892-391c-11dd-90d9-001a92567626",
        CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626",
        Weight=1.2,
        ServiceType="WarehouseWarehouse",
        CargoType="Cargo",
        SeatsAmount=1
    )
    response = mock_api.internet_document.get_document_price(request)

    # Assertions
    assert response.Cost == 150.50
    assert response.AssessedCost == 500.00
    assert response.CostRedelivery == 75.25
    mock_api.internet_document.get_document_price.assert_called_once_with(request)


def test_get_document_delivery_date(mock_api):
    mock_response = Mock()
    mock_response.DeliveryDate = "20.03.2025"
    mock_api.internet_document.get_document_delivery_date.return_value = mock_response

    # Execute test
    request = DocumentDeliveryDateRequest(
        ServiceType="WarehouseWarehouse",
        CitySender="db5c8892-391c-11dd-90d9-001a92567626",
        CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626"
    )
    response = mock_api.internet_document.get_document_delivery_date(request)

    # Assertions
    assert response.DeliveryDate == "20.03.2025"
    mock_api.internet_document.get_document_delivery_date.assert_called_once_with(request)


def test_save_internet_document(mock_api):
    mock_response = Mock()
    mock_response.Ref = "test-document-ref-123"
    mock_api.internet_document.save_internet_document.return_value = mock_response

    request = SaveInternetDocumentRequest(
        PayerType="Sender",
        PaymentMethod="Cash",
        DateTime="18.03.2025",
        CargoType="Cargo",
        Weight=5.0,
        ServiceType="WarehouseWarehouse",
        SeatsAmount=1,
        Description="Тестовый груз",
        Cost=500,
        CitySender="8d5a980d-391c-11dd-90d9-001a92567626",
        Sender="sender-ref-123",
        SenderAddress="sender-address-ref-123",
        ContactSender="contact-sender-ref-123",
        SendersPhone="380660000000",
        CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626",
        Recipient="recipient-ref-123",
        RecipientAddress="recipient-address-ref-123",
        ContactRecipient="contact-recipient-ref-123",
        RecipientsPhone="380661111111"
    )
    response = mock_api.internet_document.save_internet_document(request)

    # Assertions
    assert response.Ref == "test-document-ref-123"
    mock_api.internet_document.save_internet_document.assert_called_once_with(request)


def test_get_document_list(mock_api):
    # Setup mock response
    mock_documents = [Mock(Ref="doc1"), Mock(Ref="doc2")]
    mock_api.internet_document.get_document_list.return_value = mock_documents

    # Execute test
    request = DocumentListRequest(
        DateTimeFrom="01.03.2025",
        DateTimeTo="31.03.2025"
    )
    response = mock_api.internet_document.get_document_list(request)

    # Assertions
    assert len(response) == 2
    assert response[0].Ref == "doc1"
    assert response[1].Ref == "doc2"
    mock_api.internet_document.get_document_list.assert_called_once_with(request)


def test_delete_internet_document(mock_api):
    # Setup mock response
    mock_response = Mock()
    mock_response.Ref = "deleted-doc-ref-123"
    mock_api.internet_document.delete_internet_document.return_value = mock_response

    # Execute test
    request = DeleteInternetDocumentRequest(DocumentRefs=["doc-ref-to-delete"])
    response = mock_api.internet_document.delete_internet_document(request)

    # Assertions
    assert response.Ref == "deleted-doc-ref-123"
    mock_api.internet_document.delete_internet_document.assert_called_once_with(request)
