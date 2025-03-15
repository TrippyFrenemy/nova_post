import os
import pytest
from dotenv import load_dotenv
from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError

load_dotenv()


@pytest.fixture
def api():
    api_key = os.getenv("NOVA_POST_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан API-ключ для интеграционных тестов!")
    return NovaPostApi(api_key)


def test_track_parcel_not_found(api):
    tracking_number = "20400048799000"

    try:
        result = api.tracking.track_parcel(tracking_number=tracking_number)
        print(result)
        assert result.Number == tracking_number
        assert result.Status == "Номер не знайдено"
    except NovaPostApiError as e:
        pytest.fail(f"API returned error: {e}")


def test_track_parcel_delivered(api):
    tracking_number = os.getenv("NOVA_POST_TRACKING_NUMBER")

    try:
        result = api.tracking.track_parcel(tracking_number=tracking_number)
        print(result)
        assert result.Number == tracking_number
        assert result.Status == "Відправлення отримано"
    except NovaPostApiError as e:
        pytest.fail(f"API returned error: {e}")
