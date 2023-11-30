import pytest
import requests
from utils.requests_to_api import get_location


@pytest.mark.parametrize("city", ['New York', 'Los Angeles', 'Ohio'])
def test_get_location(city):
    response = get_location(city)
    print(response)
    assert response['status'] == 200
