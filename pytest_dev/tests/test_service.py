import pytest
import requests

import pytest_dev.source.service as service
import unittest.mock as mock


@mock.patch("pytest_dev.source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Anne"

    print('\n\n'+mock_get_user_from_db)
    print('\n'+mock_get_user_from_db.return_value)
    user_name = service.get_user_from_db(1)
    print(user_name)

    assert user_name == "Mocked Anne"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response

    data = service.get_users()

    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
