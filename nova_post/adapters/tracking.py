from typing import Optional
from ..models.tracking import ParcelStatus


class Tracking:
    def __init__(self, api):
        self.api = api

    def track_parcel(self, tracking_number: str, phone: Optional[str] = None) -> ParcelStatus:
        """Отслеживание посылки по номеру отправления и (опционально) номеру телефона"""
        properties = {
            "Documents": [{"DocumentNumber": tracking_number}]
        }

        if phone:
            properties["Documents"][0]["Phone"] = phone

        result = self.api.send_request("TrackingDocument", "getStatusDocuments", properties)
        return ParcelStatus(**result[0])
