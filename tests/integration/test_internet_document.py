import os

import pytest
from dotenv import load_dotenv

from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError
from nova_post.logger import logger
from nova_post.models.contact_person import GetContactPersonRequest
from nova_post.models.counterparty import GetCounterpartiesRequest, \
    CounterpartyAddressRequest
from nova_post.models.internet_document import (
    DocumentPriceRequest, DocumentDeliveryDateRequest,
    SaveInternetDocumentRequest, DocumentListRequest,
    DeleteInternetDocumentRequest
)

load_dotenv()


@pytest.fixture
def api():
    api_key = os.getenv("NOVA_POST_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан API-ключ для интеграционных тестов!")
    return NovaPostApi(api_key)


def get_valid_counterparty(api, counterparty_property="Sender"):
    counterparties = api.counterparty.get_counterparties(counterparty_property)
    assert counterparties, "Нет доступных контрагентов"
    return counterparties[0].Ref


def test_get_document_price(api):
    try:
        request = DocumentPriceRequest(
            CitySender="db5c8892-391c-11dd-90d9-001a92567626",
            CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626",
            Weight=1.2,
            ServiceType="WarehouseWarehouse",
            CargoType="Cargo",
            SeatsAmount=1
        )
        response = api.internet_document.get_document_price(request)
        assert response.Cost is not None
        response.Cost = str(response.Cost)
        response.AssessedCost = str(response.AssessedCost)
        if response.CostRedelivery is not None:
            response.CostRedelivery = str(response.CostRedelivery)
        logger.info(response)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_document_delivery_date(api):
    try:
        request = DocumentDeliveryDateRequest(
            ServiceType="WarehouseWarehouse",
            CitySender="db5c8892-391c-11dd-90d9-001a92567626",
            CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626"
        )
        response = api.internet_document.get_document_delivery_date(request)
        assert response.DeliveryDate is not None
        if isinstance(response.DeliveryDate, dict):
            response.DeliveryDate = response.DeliveryDate.get("date", "")
        logger.info(response)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_save_internet_document(api):
    try:
        # Отримуємо всіх контрагентів
        sender_list = api.counterparty.get_counterparties(GetCounterpartiesRequest(CounterpartyProperty="Sender"))
        recipient_list = api.counterparty.get_counterparties(GetCounterpartiesRequest(CounterpartyProperty="Recipient"))

        assert sender_list, "Не знайдено жодного відправника!"
        assert recipient_list, "Не знайдено жодного одержувача!"

        # Беремо першого контрагента
        sender_ref = GetContactPersonRequest(Ref=sender_list[0].Ref)
        recipient_ref = GetContactPersonRequest(Ref=recipient_list[0].Ref)

        print(f"Вибрано контрагента Sender: {sender_ref}")
        print(f"Вибрано контрагента Recipient: {recipient_ref}")

        # Отримуємо контактні особи першого контрагента
        sender_contacts = api.counterparty.get_counterparty_contact_persons(sender_ref)
        recipient_contacts = api.counterparty.get_counterparty_contact_persons(recipient_ref)

        assert sender_contacts, "Контрагент Sender не має контактних осіб!"
        assert recipient_contacts, "Контрагент Recipient не має контактних осіб!"

        # Шукаємо контакт з ім'ям "Тест"
        contact_sender_ref = None
        contact_recipient_ref = None

        for contact in sender_contacts:
            if contact.FirstName == "Дмитро":
                contact_sender_ref = contact.Ref
                break

        for contact in recipient_contacts:
            if contact.FirstName == "Тест":
                contact_recipient_ref = contact.Ref
                break

        # Якщо контакт "Тест" не знайдено – беремо 5-й контакт (якщо є)
        if not contact_sender_ref and len(sender_contacts) >= 5:
            contact_sender_ref = sender_contacts[4].Ref
        if not contact_recipient_ref and len(recipient_contacts) >= 5:
            contact_recipient_ref = recipient_contacts[4].Ref

        assert contact_sender_ref, "Не знайдено контакт 'Тест' або 5-й контакт у Sender!"
        assert contact_recipient_ref, "Не знайдено контакт 'Тест' або 5-й контакт у Recipient!"

        print(f"Вибрано контакт Sender: {contact_sender_ref}")
        print(f"Вибрано контакт Recipient: {contact_recipient_ref}")

        sender = CounterpartyAddressRequest(Ref=sender_ref.Ref, CounterpartyProperty="Sender")
        recipient = CounterpartyAddressRequest(Ref=recipient_ref.Ref, CounterpartyProperty="Recipient")
        # Отримуємо адреси контрагентів
        sender_addresses = api.counterparty.get_counterparty_addresses(sender)
        recipient_addresses = api.counterparty.get_counterparty_addresses(recipient)

        sender_address_ref = sender_addresses[0].Ref if sender_addresses else None
        recipient_address_ref = recipient_addresses[0].Ref if recipient_addresses else None

        print(f"Адреса Sender: {sender_address_ref}")
        print(f"Адреса Recipient: {recipient_address_ref}")

        # Формуємо запит
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
            Sender=sender_ref.Ref,
            SenderAddress=sender_address_ref,
            ContactSender=contact_sender_ref,
            SendersPhone="380660000000",
            CityRecipient="8d5a980d-391c-11dd-90d9-001a92567626",
            Recipient=recipient_ref.Ref,
            RecipientAddress=sender_address_ref,
            ContactRecipient=contact_recipient_ref,
            RecipientsPhone="380661111111"
        )

        response = api.internet_document.save_internet_document(request)
        assert response.Ref is not None
        print(f"Збережено документ: {response.Ref}")

    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_get_document_list(api):
    try:
        request = DocumentListRequest(
            DateTimeFrom="01.03.2025",
            DateTimeTo="31.03.2025"
        )
        response = api.internet_document.get_document_list(request)
        assert isinstance(response, list)
        logger.info(response)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")


def test_delete_internet_document(api):
    try:
        # Получаем список существующих накладных
        request_list = DocumentListRequest(DateTimeFrom="01.03.2025", DateTimeTo="31.03.2025")
        documents = api.internet_document.get_document_list(request_list)
        if not documents:
            pytest.skip("Нет доступных накладных для удаления")
        request = DeleteInternetDocumentRequest(DocumentRefs=[documents[0].Ref])
        response = api.internet_document.delete_internet_document(request)
        assert response.Ref is not None
        logger.info(response)
    except NovaPostApiError as e:
        pytest.fail(f"API вернул ошибку: {e}")
