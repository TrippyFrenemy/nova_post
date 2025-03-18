from typing import List, Optional

from ..models.contact_person import (
    ContactPersonRequest,
    ContactPersonResponse, DeleteContactPersonRequest, GetContactPersonRequest
)
from ..models.counterparty import (
    CounterpartyRequest,
    CounterpartyResponse,
    GetCounterpartiesResponse, GetCounterpartiesRequest, DeleteCounterpartiesRequest, CounterpartyAddressResponse,
    CounterpartyAddressRequest, CounterpartyOptionsResponse, CounterpartyOptionsRequest,
)


class Counterparty:
    """
    Адаптер для роботи з контрагентами та їх контактними особами.

    Дозволяє створювати, оновлювати, видаляти контрагентів, отримувати список контрагентів,
    їх контактних осіб та адреси.
    """

    def __init__(self, api):
        self.api = api

    def save(self, data: CounterpartyRequest) -> CounterpartyResponse:
        """
        Створення контрагента (Фізична особа, Третя особа, Організація).

        :param data: Pydantic-модель `CounterpartyRequest`, що містить інформацію про контрагента.
        :return: Об'єкт `CounterpartyResponse` із даними створеного контрагента.
        """
        result = self.api.send_request("Counterparty", "save", data.model_dump(exclude_unset=True))
        return CounterpartyResponse.model_validate(result[0]) if result else CounterpartyResponse()

    def get_counterparties(self, data: GetCounterpartiesRequest) -> List[GetCounterpartiesResponse]:
        """
        Отримання списку контрагентів (відправників, отримувачів, третіх осіб).

        :param data: Pydantic-модель `GetCounterpartiesRequest` із параметрами пошуку.
        :return: Список об'єктів `GetCounterpartiesResponse` із даними контрагентів.
        """
        result = self.api.send_request("Counterparty", "getCounterparties", data.model_dump(exclude_unset=True))
        return [GetCounterpartiesResponse.model_validate(cp) for cp in result]

    def update(self, data: CounterpartyRequest) -> CounterpartyResponse:
        """
        Оновлення даних контрагента.

        :param data: Pydantic-модель `CounterpartyRequest` із новими даними контрагента.
        :return: Об'єкт `CounterpartyResponse` із оновленими даними контрагента.
        """
        result = self.api.send_request("Counterparty", "update", data.model_dump(exclude_unset=True))
        return CounterpartyResponse.model_validate(result[0]) if result else CounterpartyResponse()

    def delete(self, data: DeleteCounterpartiesRequest) -> bool:
        """
        Видалення контрагента.

        :param data: Pydantic-модель `DeleteCounterpartiesRequest` із `Ref` контрагента.
        :return: `True`, якщо видалення успішне.
        """
        result = self.api.send_request("Counterparty", "delete", data.model_dump(exclude_unset=True))
        return bool(result)

    def get_counterparty_addresses(self, data: CounterpartyAddressRequest) -> List[CounterpartyAddressResponse]:
        """
        Отримання списку адрес контрагента.

        :param data: Pydantic-модель `CounterpartyAddressRequest`, що містить `Ref` контрагента.
        :return: Список об'єктів `CounterpartyAddressResponse` із адресами контрагента.
        """
        result = self.api.send_request("Counterparty", "getCounterpartyAddresses", data.model_dump(exclude_unset=True))
        return [CounterpartyAddressResponse.model_validate(addr) for addr in result]

    def get_counterparty_options(self, data: CounterpartyOptionsRequest) -> Optional[CounterpartyOptionsResponse]:
        """
        Отримання параметрів контрагента.

        :param data: Pydantic-модель `CounterpartyOptionsRequest`, що містить `Ref` контрагента.
        :return: Об'єкт `CounterpartyOptionsResponse` із можливостями контрагента або `None`, якщо дані відсутні.
        """
        result = self.api.send_request("Counterparty", "getCounterpartyOptions", data.model_dump(exclude_unset=True))
        return CounterpartyOptionsResponse.model_validate(result[0]) if result else None

    def get_counterparty_contact_persons(self, data: GetContactPersonRequest) -> List[ContactPersonResponse]:
        """
        Отримання списку контактних осіб контрагента.

        :param data: Pydantic-модель `GetContactPersonRequest`, що містить `Ref` контрагента та `Page`.
        :return: Список об'єктів `ContactPersonResponse` із контактними особами контрагента.
        """
        result = self.api.send_request("Counterparty", "getCounterpartyContactPersons",
                                       data.model_dump(exclude_unset=True))
        return [ContactPersonResponse.model_validate(item) for item in result]

    def save_contact_person(self, data: ContactPersonRequest) -> ContactPersonResponse:
        """
        Створення контактної особи контрагента.

        :param data: Pydantic-модель `ContactPersonRequest` із даними контактної особи.
        :return: Об'єкт `ContactPersonResponse` із даними створеної контактної особи.
        """
        result = self.api.send_request("ContactPerson", "save", data.model_dump(exclude_unset=True))
        return ContactPersonResponse.model_validate(result[0]) if result else ContactPersonResponse()

    def update_contact_person(self, data: ContactPersonRequest) -> ContactPersonResponse:
        """
        Оновлення контактної особи контрагента.

        :param data: Pydantic-модель `ContactPersonRequest`, що містить нові дані контактної особи.
        :return: Об'єкт `ContactPersonResponse` із оновленими даними контактної особи.
        """
        result = self.api.send_request("ContactPerson", "update", data.model_dump(exclude_unset=True))
        return ContactPersonResponse.model_validate(result[0]) if result else ContactPersonResponse()

    def delete_contact_person(self, data: DeleteContactPersonRequest) -> bool:
        """
        Видалення контактної особи контрагента.

        :param data: Pydantic-модель `DeleteContactPersonRequest`, що містить `Ref` контактної особи.
        :return: `True`, якщо контактна особа успішно видалена.
        """
        result = self.api.send_request("ContactPerson", "delete", data.model_dump(exclude_unset=True))
        return bool(result)
