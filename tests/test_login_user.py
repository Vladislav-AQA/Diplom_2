import requests
import pytest
import allure
from helpers import urls
from helpers import data
from faker import Faker

fake = Faker(locale="ru_RU")


@allure.title('Проверка логина пользователя')
class TestLoginUser:

    @allure.description('Получение статус-кода при успешном логине пользователя')
    def test_login_exist_user(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = requests.post(urls.LOGIN_USER, response.json().get('accessToken'))

        assert response.status_code == 200

    @allure.description('Получение статус-кода с неверным логином и паролем')
    def test_required_login_password(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        email = response.get('email', '')
        password = response.get('password', '')
        access_token = requests.post(urls.LOGIN_USER, response.get('email', fake.email()), response.get('password', fake.password()))

        assert access_token == 401