import allure
import requests
import pytest
from helpers import urls
from helpers import data
from helpers.data import Data


@allure.title('Редактирование данных пользователя')
class TestEditUser:
    @allure.description('Получение статус-кода при изменении данных пользователя с авторизацией')
    @pytest.mark.parametrize('value', ['email', 'password'])
    def test_edit_user(self, value):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        email = response.get('email', '')
        password = response.get('password', '')
        login = requests.post(urls.LOGIN_USER(response.get('email', email), response.get('password', password)))
        access_token = login.json().get('accessToken')

        update_user = response.copy()
        if value == "email":
            update_user['email'] = data.Data.NEW_EMAIL_USER
        elif value == "name":
            update_user['name'] = data.Data.NEW_NAME_USER

        update_response = response(access_token, update_user)

        assert update_response.status_code == 200

    @allure.description('Получение статус-кода при изменении данных пользователя без авторизации')
    def test_edit_no_auth_user(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        email = response.get('email', '')
        password = response.get('password', '')
        login = requests.post(urls.LOGIN_USER(response.get('email', email), response.get('password', password)))
        access_token = None

        update_user = response.copy()
        if value == "email":
            update_user['email'] = data.Data.NEW_EMAIL_USER
        elif value == "name":
            update_user['name'] = data.Data.NEW_NAME_USER

        update_response = response(access_token, update_user)

        assert update_response.status_code == 401




