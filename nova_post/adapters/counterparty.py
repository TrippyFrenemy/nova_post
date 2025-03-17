from typing import List, Optional

from ..models.contact_person import (
    ContactPersonRequest,
    ContactPersonResponse
)
from ..models.counterparty import (
    CounterpartyRequest,
    CounterpartyResponse,
    CounterpartyOptions,
    CounterpartyAddress,
    GetCounterpartiesResponse,
)


class Counterparty:
    """
    Адаптер для работы с контрагентами и (по желанию) их контактными лицами.
    """

    def __init__(self, api):
        self.api = api

    def save(self, data: CounterpartyRequest) -> CounterpartyResponse:
        """
        Создание контрагента (PrivatePerson, ThirdPerson, Organization).
        В зависимости от заполненных полей:
         - FirstName, LastName, MiddleName => физ. лицо
         - EDRPOU => организация
         - И т.д.
        Документация: метод «save» для модели «Counterparty».
        """
        # Формируем словарь properties на основе pydantic-модели
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("Counterparty", "save", properties)
        if not result:
            return CounterpartyResponse()  # Пустое значение, если нет ответа
        return CounterpartyResponse.model_validate(result[0])

    def get_counterparties(
            self,
            counterparty_property: str,
            page: Optional[int] = None,
            find_by_string: Optional[str] = None
    ) -> List[GetCounterpartiesResponse]:
        """
        Получить список контрагентов (получателей, отправителей, третьих лиц).
        Документация: метод «getCounterparties».
        """
        properties = {
            "CounterpartyProperty": counterparty_property
        }
        if page:
            properties["Page"] = page
        if find_by_string:
            properties["FindByString"] = find_by_string

        result = self.api.send_request("Counterparty", "getCounterparties", properties)
        return [GetCounterpartiesResponse.model_validate(cp) for cp in result]

    def update(self, data: CounterpartyRequest) -> CounterpartyResponse:
        """
        Обновление данных контрагента.
        Документация: метод «update» для модели «Counterparty».
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("Counterparty", "update", properties)
        if not result:
            return CounterpartyResponse()
        return CounterpartyResponse.model_validate(result[0])

    def delete(self, ref: str) -> bool:
        """
        Удалить контрагента-одержувача.
        Документация: метод «delete» для модели «Counterparty».
        """
        properties = {"Ref": ref}
        result = self.api.send_request("Counterparty", "delete", properties)
        return bool(result)

    def get_counterparty_addresses(self, ref: str, counterparty_property: str) -> List[CounterpartyAddress]:
        """
        Загрузка списка адресов контрагента.
        Документация: метод «getCounterpartyAddresses».
        """
        properties = {
            "Ref": ref,
            "CounterpartyProperty": counterparty_property
        }
        result = self.api.send_request("Counterparty", "getCounterpartyAddresses", properties)
        return [CounterpartyAddress.model_validate(addr) for addr in result]

    def get_counterparty_options(self, ref: str) -> Optional[CounterpartyOptions]:
        """
        Получить параметры контрагента.
        Документация: метод «getCounterpartyOptions».
        """
        properties = {"Ref": ref}
        result = self.api.send_request("Counterparty", "getCounterpartyOptions", properties)
        if not result:
            return None
        # Предполагаем, что result[0] содержит данные об опциях
        return CounterpartyOptions.model_validate(result[0])

    def get_counterparty_contact_persons(
            self,
            ref: str,
            page: Optional[int] = None
    ) -> List[ContactPersonResponse]:
        """
        Получить список контактных лиц контрагента.
        Документация: «getCounterpartyContactPersons» (модель «Counterparty»).
        """
        properties = {"Ref": ref}
        if page:
            properties["Page"] = page
        result = self.api.send_request("Counterparty", "getCounterpartyContactPersons", properties)
        return [ContactPersonResponse.model_validate(item) for item in result]

    def save_contact_person(self, data: ContactPersonRequest) -> ContactPersonResponse:
        """
        Создать контактное лицо контрагента.
        Документация: метод «save» (модель «ContactPerson»).
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("ContactPerson", "save", properties)
        if not result:
            return ContactPersonResponse(Ref="", Description="")
        return ContactPersonResponse.model_validate(result[0])

    def update_contact_person(self, data: ContactPersonRequest) -> ContactPersonResponse:
        """
        Обновить контактное лицо контрагента.
        Документация: метод «update» (модель «ContactPerson»).
        """
        properties = data.model_dump(exclude_unset=True)
        result = self.api.send_request("ContactPerson", "update", properties)
        if not result:
            return ContactPersonResponse(Ref="", Description="")
        return ContactPersonResponse.model_validate(result[0])

    def delete_contact_person(self, ref: str) -> bool:
        """
        Удалить контактное лицо контрагента.
        Документация: метод «delete» (модель «ContactPerson»).
        """
        properties = {"Ref": ref}
        result = self.api.send_request("ContactPerson", "delete", properties)
        return bool(result)
