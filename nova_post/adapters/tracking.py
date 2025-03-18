from ..models.tracking import TrackingRequest, TrackingResponse


class Tracking:
    """
    Адапртер для відстеження відправлення
    """

    def __init__(self, api):
        self.api = api

    def track_parcel(self, data: TrackingRequest) -> TrackingResponse:
        """
        Відстеження посилки за номером експрес-накладної та (опціонально) номером телефону.

        :param data: Pydantic-модель `TrackingRequest`, що містить номер відправлення та (необов'язково) номер телефону.
        :return: Об'єкт `TrackingResponse`, що містить інформацію про статус відправлення.
        """
        properties = {
            "Documents": [data.model_dump(exclude_unset=True)]
        }

        result = self.api.send_request("TrackingDocument", "getStatusDocuments", properties)
        return TrackingResponse.model_validate(result[0])
