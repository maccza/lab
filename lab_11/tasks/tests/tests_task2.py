import pytest
from lab_11.tasks.tools.metaweather import (
    get_metaweather
)
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import Mock
from lab_11.tasks.tools.metaweather import get_metaweather, get_cities_woeid
import requests


def test_get_cities_woeid():
    value_to_mock = Mock()

    value_to_mock.status = 200

    value_to_mock.json.return_value = [
        {"title": "Warsaw", "woeid": 523920},
        {"title": "Newark", "woeid": 2459269},
    ]

    with patch("requests.get", return_value=value_to_mock) as mock_fun: 
        assert get_cities_woeid("War") == {
            "Warsaw": 523920,
            "Newark": 2459269,
        }

