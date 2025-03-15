from ..models.tracking import ParcelStatus


class Tracking:
    def __init__(self, api):
        self.api = api

    def track_parcel(self, tracking_number: str) -> ParcelStatus:
        properties = {"Documents": [{"DocumentNumber": tracking_number}]}
        result = self.api.send_request("TrackingDocument", "getStatusDocuments", properties)
        return ParcelStatus(**result[0])
