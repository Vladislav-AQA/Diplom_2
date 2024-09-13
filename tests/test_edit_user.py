import allure
import requests
import pytest
from helpers import new_data
from helpers.user import User


@allure.title('Редактирование данных пользователя')
class TestEditUser:
    @allure.description('Получение статус-кода при изменении данных пользователя с авторизацией')
    @pytest.mark.parametrize('value', ['email', 'name'])
    def test_edit_user(self, value, create_delete_user):
        user_data = create_delete_user
        email = user_data.get('email', '')
        password = user_data.get('password', '')
        login = User.log_in(user_data.get('email', email), user_data.get('password', password))
        access_token = login.json().get('accessToken')

        update_user = user_data.copy()
        if value == "email":
            update_user['email'] = new_data.NEW_EMAIL
        elif value == "name":
            update_user['name'] = new_data.NEW_NAME

        update_response = User.edit_data_user(access_token, update_user)

        assert update_response.status_code == 200

    @allure.description('Получение статус-кода при изменении данных пользователя без авторизации')
    @pytest.mark.parametrize('value', ['email', 'name'])
    def test_edit_no_auth_user(self, value, create_delete_user):
        user_data = create_delete_user
        email = user_data.get('email', '')
        password = user_data.get('password', '')
        User.log_in(user_data.get('email', email), user_data.get('password', password))
        access_token = None

        update_user = user_data.copy()
        if value == "email":
            update_user['email'] = new_data.NEW_EMAIL
        elif value == "name":
            update_user['name'] = new_data.NEW_NAME

        update_response = User.edit_data_user(access_token, update_user)

        assert update_response.status_code == 401




