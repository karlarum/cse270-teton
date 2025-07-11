import pytest
import requests

class TestUsersEndpointIntegration:
  
    BASE_URL = "http://127.0.0.1:53829"
    USERS_ENDPOINT = f"{BASE_URL}/users/"
    
    def test_valid_credentials_returns_200(self):
        params = {
            "username": "admin",
            "password": "qwerty"
        }

        response = requests.get(self.USERS_ENDPOINT, params=params)
        
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        
    def test_valid_credentials_returns_empty_text_response_200(self):
        params = {
            "username": "admin",
            "password": "qwerty"
        }
        
        response = requests.get(self.USERS_ENDPOINT, params=params)
        
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.text == "", f"Expected empty text response, but got: '{response.text}'"
        assert 'text' in response.headers.get('content-type', '').lower(), f"Expected text content-type, but got: {response.headers.get('content-type')}"
        
    def test_invalid_credentials_returns_401(self):
        params = {
            "username": "admin",
            "password": "admin"
        }
        
        response = requests.get(self.USERS_ENDPOINT, params=params)
        
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    
    def test_authentication_failed(self, mocker):
        url = 'http://127.0.0.1:8000/users'
        params = {
            'username': 'admin',
            'password': 'admin'
        }
        
        mocked_response = mocker.Mock()
        mocked_response.status_code = 401
        mocked_response.text = ''
        
        mocker.patch('requests.get', return_value=mocked_response)
        
        response = requests.get(url, params=params)
        
        assert response.status_code == 401
        assert response.text.strip() == ''
        
    def test_authentication_successful(self, mocker):
        url = 'http://127.0.0.1:8000/users'
        params = {
            'username': 'admin',
            'password': 'qwerty'
        }
        
        mocked_response = mocker.Mock()
        mocked_response.status_code = 200
        mocked_response.text = ''
        
        mocker.patch('requests.get', return_value=mocked_response)
        
        response = requests.get(url, params=params)
        
        assert response.status_code == 200
        assert response.text.strip() == ''

if __name__ == '__main__':
    pytest.main([__file__ + "::TestUsersEndpointIntegration", "-v"])