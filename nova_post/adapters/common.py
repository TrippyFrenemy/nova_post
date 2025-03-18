from typing import List

from nova_post.models.common import (TimeIntervalRequest, TimeIntervalResponse, CargoTypeResponse, PalletResponse,
                                     PayerForRedeliveryResponse, PackListResponse, TiresWheelsResponse,
                                     CargoDescriptionResponse, ServiceTypeResponse,
                                     OwnershipFormResponse)


class Common:
    """
    Адаптер для роботи з довідниками
    """

    def __init__(self, api):
        self.api = api

    def get_time_intervals(self, data: TimeIntervalRequest) -> List[TimeIntervalResponse]:
        """
        Отримання списку часових інтервалів для замовлення послуги "Часові інтервали".

        :param data: Pydantic-модель `TimeIntervalRequest`, що містить `RecipientCityRef` для фільтрації за містом.
        :return: Список об'єктів `TimeIntervalResponse` із часовими інтервалами.
        """
        result = self.api.send_request("Common", "getTimeIntervals", data.model_dump(exclude_unset=True))
        return [TimeIntervalResponse.model_validate(item) for item in result]

    def get_cargo_types(self) -> List[CargoTypeResponse]:
        """
        Отримання списку типів вантажу.

        :return: Список об'єктів `CargoTypeResponse`, що містять опис доступних типів вантажу.
        """
        result = self.api.send_request("Common", "getCargoTypes", {})
        return [CargoTypeResponse.model_validate(item) for item in result]

    def get_pallets_list(self) -> List[PalletResponse]:
        """
        Отримання списку доступних видів палет.

        :return: Список об'єктів `PalletResponse`, що містять опис палет.
        """
        result = self.api.send_request("Common", "getPalletsList", {})
        return [PalletResponse.model_validate(item) for item in result]

    def get_types_of_payers_for_redelivery(self) -> List[PayerForRedeliveryResponse]:
        """
        Отримання списку типів платників зворотної доставки.

        :return: Список об'єктів `PayerForRedeliveryResponse`, що містять інформацію про платників зворотної доставки.
        """
        result = self.api.send_request("Common", "getTypesOfPayersForRedelivery", {})
        return [PayerForRedeliveryResponse.model_validate(item) for item in result]

    def get_pack_list(self) -> List[PackListResponse]:
        """
        Отримання списку доступних варіантів упаковки.

        :return: Список об'єктів `PackListResponse`, що містять інформацію про види упаковки.
        """
        result = self.api.send_request("Common", "getPackList", {})
        return [PackListResponse.model_validate(item) for item in result]

    def get_tires_wheels_list(self) -> List[TiresWheelsResponse]:
        """
        Отримання списку доступних шин і дисків.

        :return: Список об'єктів `TiresWheelsResponse`, що містять інформацію про шини та диски.
        """
        result = self.api.send_request("Common", "getTiresWheelsList", {})
        return [TiresWheelsResponse.model_validate(item) for item in result]

    def get_cargo_description_list(self) -> List[CargoDescriptionResponse]:
        """
        Отримання списку доступних описів вантажу.

        :return: Список об'єктів `CargoDescriptionResponse`, що містять інформацію про доступні типи вантажів.
        """
        result = self.api.send_request("Common", "getCargoDescriptionList", {})
        return [CargoDescriptionResponse.model_validate(item) for item in result]

    def get_service_types(self) -> List[ServiceTypeResponse]:
        """
        Отримання списку доступних видів технологій доставки.

        :return: Список об'єктів `ServiceTypeResponse`, що містять інформацію про технології доставки.
        """
        result = self.api.send_request("Common", "getServiceTypes", {})
        return [ServiceTypeResponse.model_validate(item) for item in result]

    def get_ownership_forms_list(self) -> List[OwnershipFormResponse]:
        """
        Отримання списку доступних форм власності.

        :return: Список об'єктів `OwnershipFormResponse`, що містять інформацію про форми власності.
        """
        result = self.api.send_request("Common", "getOwnershipFormsList", {})
        return [OwnershipFormResponse.model_validate(item) for item in result]
