from unittest.mock import MagicMock

import pytest

from nova_post.api import NovaPostApi
from nova_post.models.contact_person import ContactPersonRequest, DeleteContactPersonRequest
from nova_post.models.counterparty import CounterpartyRequest


@pytest.fixture
def api():
    """
    Фикстура, возвращающая объект NovaPostApi.
    Здесь он не требует реального api_key, так как мы будем мокать send_request.
    """
    return NovaPostApi(api_key="test-key")


def test_save_private_person_mock(api):
    """
    Мок-тест на создание контрагента-физлица (PrivatePerson).
    """
    # Готовим "фейковый" ответ, который обычно возвращает реальное API
    # Обратите внимание, что ваша логика в api.py проверяет 'success' и 'data'
    mock_response = {
        "success": True,
        "data": [
            {
                "Ref": "mock-private-person-ref",
                "Description": "Тест Тестович Тестов",
                "FirstName": "Тест",
                "MiddleName": "Тестович",
                "LastName": "Тестов",
            }
        ],
        "errors": [],
        "warnings": [],
        "info": []
    }

    # Делаем функцию, которая возвращает этот фейковый ответ при любом вызове send_request
    def mock_send_request(model, method, properties):
        return mock_response["data"] if mock_response["success"] else []

    # Подменяем метод send_request в экземпляре api на нашу mock-функцию
    api.send_request = MagicMock(side_effect=mock_send_request)

    # Создаём тестовые данные
    data = CounterpartyRequest(
        FirstName="Тест",
        MiddleName="Тестович",
        LastName="Тестов",
        Phone="380501112233",
        CounterpartyType="PrivatePerson",
        CounterpartyProperty="Recipient"
    )

    # Вызываем реальный метод адаптера, но под капотом запрос будет замокан
    result = api.counterparty.save(data)

    # Проверяем, что метод send_request действительно вызывался
    api.send_request.assert_called_once()

    # Проверяем результат
    assert result.Ref == "mock-private-person-ref"
    assert result.FirstName == "Тест"
    assert result.LastName == "Тестов"


def test_save_third_person_mock(api):
    """
    Мок-тест на создание контрагента «третья сторона» (Organization).
    """
    # Здесь «CounterpartyType» = "Organization", «CounterpartyProperty» = "ThirdPerson"
    mock_response = {
        "success": True,
        "data": [
            {
                "Ref": "mock-third-person-ref",
                "Description": "ООО «Третья сторона»",
                "EDRPOU": "12345678",
                "CounterpartyType": "Organization",
            }
        ],
        "errors": [],
        "warnings": [],
        "info": []
    }

    def mock_send_request(model, method, properties, timeout=10):
        return mock_response["data"] if mock_response["success"] else []

    api.send_request = MagicMock(side_effect=mock_send_request)

    data = CounterpartyRequest(
        FirstName="",
        MiddleName="",
        LastName="",
        EDRPOU="12345678",
        CounterpartyType="Organization",
        CounterpartyProperty="ThirdPerson"
    )

    result = api.counterparty.save(data)

    # Снова проверяем что send_request был вызван, и сверяем результат
    api.send_request.assert_called_once()
    assert result.Ref == "mock-third-person-ref"
    assert result.EDRPOU == "12345678"
    assert result.CounterpartyType == "Organization"


def test_create_and_delete_contact_person_mock(api):
    """
    Мок-тест на создание и удаление контактного лица.
    """
    # 1) Мок для saveContactPerson
    mock_save_response = {
        "success": True,
        "data": [
            {
                "Ref": "mock-contact-ref",
                "Description": "Контакт Тест",
                "LastName": "Тест",
                "FirstName": "Контакт",
                "MiddleName": "Контактный",
                "Phones": "380990000000"
            }
        ],
        "errors": [],
        "warnings": [],
        "info": []
    }

    # 2) Мок для deleteContactPerson
    mock_delete_response = {
        "success": True,
        "data": [
            {
                "Ref": "mock-contact-ref"
            }
        ],
        "errors": [],
        "warnings": [],
        "info": []
    }

    # Будем переключаться между двумя разными ответами в зависимости от вызова
    def mock_send_request(model, method, properties, timeout=10):
        if method == "save":
            return mock_save_response["data"]
        elif method == "delete":
            return mock_delete_response["data"]
        return []

    api.send_request = MagicMock(side_effect=mock_send_request)

    # Создаём контакт
    contact_data = ContactPersonRequest(
        CounterpartyRef="mock-counterparty-ref",
        FirstName="Контакт",
        LastName="Тест",
        MiddleName="Контактный",
        Phone="380990000000"
    )
    new_cp = api.counterparty.save_contact_person(contact_data)

    # Проверяем, что контакт создан
    assert new_cp.Ref == "mock-contact-ref"
    assert new_cp.FirstName == "Контакт"
    assert new_cp.LastName == "Тест"

    delete_cp = DeleteContactPersonRequest(
        Ref=new_cp.Ref
    )

    # Удаляем контакт
    deleted = api.counterparty.delete_contact_person(delete_cp)
    assert deleted is True

    # Проверяем, что метод send_request был вызван два раза
    assert api.send_request.call_count == 2
    api.send_request.assert_any_call("ContactPerson", "save", contact_data.model_dump(exclude_unset=True))
    api.send_request.assert_any_call("ContactPerson", "delete", {"Ref": "mock-contact-ref"})
