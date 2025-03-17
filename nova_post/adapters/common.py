from typing import List

from nova_post.models.common import (TimeIntervalRequest, TimeIntervalResponse, CargoTypeResponse, PalletResponse,
                                     PayerForRedeliveryResponse, PackListResponse, TiresWheelsResponse,
                                     CargoDescriptionResponse, ServiceTypeResponse,
                                     OwnershipFormResponse)


class Common:
    def __init__(self, api):
        self.api = api

    def get_time_intervals(self, data: TimeIntervalRequest) -> List[TimeIntervalResponse]:
        result = self.api.send_request("Common", "getTimeIntervals", data.model_dump(exclude_unset=True))
        return [TimeIntervalResponse.model_validate(item) for item in result]

    def get_cargo_types(self) -> List[CargoTypeResponse]:
        result = self.api.send_request("Common", "getCargoTypes", {})
        return [CargoTypeResponse.model_validate(item) for item in result]

    def get_pallets_list(self) -> List[PalletResponse]:
        result = self.api.send_request("Common", "getPalletsList", {})
        return [PalletResponse.model_validate(item) for item in result]

    def get_types_of_payers_for_redelivery(self) -> List[PayerForRedeliveryResponse]:
        result = self.api.send_request("Common", "getTypesOfPayersForRedelivery", {})
        return [PayerForRedeliveryResponse.model_validate(item) for item in result]

    def get_pack_list(self) -> List[PackListResponse]:
        result = self.api.send_request("Common", "getPackList", {})
        return [PackListResponse.model_validate(item) for item in result]

    def get_tires_wheels_list(self) -> List[TiresWheelsResponse]:
        result = self.api.send_request("Common", "getTiresWheelsList", {})
        return [TiresWheelsResponse.model_validate(item) for item in result]

    def get_cargo_description_list(self) -> List[CargoDescriptionResponse]:
        result = self.api.send_request("Common", "getCargoDescriptionList", {})
        return [CargoDescriptionResponse.model_validate(item) for item in result]

    def get_service_types(self) -> List[ServiceTypeResponse]:
        result = self.api.send_request("Common", "getServiceTypes", {})
        return [ServiceTypeResponse.model_validate(item) for item in result]

    def get_ownership_forms_list(self) -> List[OwnershipFormResponse]:
        result = self.api.send_request("Common", "getOwnershipFormsList", {})
        return [OwnershipFormResponse.model_validate(item) for item in result]
