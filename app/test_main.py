# write your code here
import pytest

from unittest import mock

from app.main import can_access_google_page

def test_if_url_is_valid():
    url = 'https://google.com'
    mocked_valid_google_url = mock.MagicMock()
    mocked_has_internet_connection = mock.MagicMock()
    assert can_access_google_page(url) == "Not accessible"
