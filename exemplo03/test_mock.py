import pytest
import requests
from unittest.mock import MagicMock

@pytest.fixture
def mock_respomse():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_velue = ["massage":"Sucess"]

def test_api_call_with_mock1(mock_respomse):
    response = mock_respomse
    assert response.status_code == 200
    assert mock.json() == ("massage":"Sucess")