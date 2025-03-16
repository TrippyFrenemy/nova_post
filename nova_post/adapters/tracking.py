from typing import Optional
from ..models.tracking import TrackingRequest, TrackingResponse


class Tracking:
    def __init__(self, api):
        self.api = api

    def track_parcel(self, data: TrackingRequest) -> TrackingResponse:
        """Отслеживание посылки по номеру отправления и (опционально) номеру телефона"""
        properties = {
            "Documents": [data.model_dump(exclude_unset=True)]
        }

        result = self.api.send_request("TrackingDocument", "getStatusDocuments", properties)
        return TrackingResponse.model_validate(result[0])
