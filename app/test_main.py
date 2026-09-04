# write your code here
from unittest import mock

from app.main import can_access_google_page


def test_if_url_is_valid() -> None:
    url = "https://google.com"
    mocked_valid_google_url = mock.MagicMock()
    mocked_has_internet_connection = mock.MagicMock()
    can_access_google_page(url)
    mocked_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()
