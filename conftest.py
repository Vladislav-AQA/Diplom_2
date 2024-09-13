import pytest
import requests
from helpers.user import User
from helpers import fake_user_and_order
from helpers import urls


@pytest.fixture()
def create_delete_user():
    user_data = fake_user_and_order.fake_user_data()
    create_response = requests.post(urls.CREATE_USER, json=user_data)
    user_access_token = create_response.json().get('accessToken')
    yield user_data
    headers_delete_user = {
        'Accept': 'application/json',
        'Authorization': user_access_token
    }
    requests.delete(urls.DELETE_USER, headers = headers_delete_user)

@pytest.fixture()
def login_user(create_delete_user):
    user_data = create_delete_user
    email = user_data.get('email', '')
    password = user_data.get('password', '')
    response_login = User.log_in(email, password)
    return response_login