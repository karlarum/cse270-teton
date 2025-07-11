import requests
import pytest

BASE_URL = "http://127.0.0.1:53829/users"

def test_authentication_failed(mocker):
    params = {
        'username': 'admin',
        'password': 'admin'  # incorrect password
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401
    assert response.text.strip() == ''


def test_authentication_successful_json(mocker):
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = '{"message": "Login successful"}'
    mocked_response.json.return_value = {"message": "Login successful"}

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200
    assert response.json()['message'] == "Login successful"


def test_authentication_successful_empty_text(mocker):
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200
    assert response.text.strip() == ''


# 👇 This is what makes `python test_user.py` work
if __name__ == "__main__":
    import sys
    import os
    # Run pytest programmatically
    sys.exit(pytest.main([os.path.abspath(__file__)]))
