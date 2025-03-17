import pytest

from nova_post.api import NovaPostApi
from nova_post.exceptions import NovaPostApiError


@pytest.fixture
def api():
    return NovaPostApi(api_key="test-key")


def test_request_timeout(api):
    """Тест: API должен выдать ошибку при таймауте"""
    with pytest.raises(NovaPostApiError, match="Таймаут запроса"):
        api.send_request("Address", "getCities", {}, timeout=0.001)
