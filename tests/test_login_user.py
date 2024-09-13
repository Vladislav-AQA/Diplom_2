import requests
import pytest
import allure
from helpers import fake_user_and_order, urls
from helpers.user import User


@allure.title('Проверка логина пользователя')
class TestLoginUser:

    @allure.description('Получение статус-кода при успешном логине пользователя')
    def test_login_exist_user(self, create_delete_user):
        user_data = create_delete_user
        response_login = User.log_in(user_data.get('email', ''), user_data.get('password', ''))
        access_token = response_login.json().get('accessToken')

        assert response_login.status_code == 200

    @allure.description('Получение статус-кода с неверным логином и паролем')
    @pytest.mark.parametrize('error', ['email', 'password'])
    def test_required_login_password(self, create_delete_user, error):
        user_data = create_delete_user.copy()
        email = user_data.get('email', '')
        password = user_data.get('password', '')
        if error == "email":
            user_data['email'] = 'qwerty@ya.ru'
        elif error == "password":
            user_data['password'] = 'qwerty1122333'

        login_response = User.log_in(user_data.get('email', email), user_data.get('password', password))

        assert login_response.status_code == 401