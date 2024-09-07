import requests
import pytest
import allure
from helpers import urls
from helpers import data
from helpers import messages



@allure.title('Проверка создания пользователя')
class TestCreateUser:
    @allure.description('Получение статус-кода 200 при создании курьера')
    def test_create_new_user(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)

        assert response.status_code == 200

    @allure.description('Получение статус-кода и сообщения об ошибке при попытке создать уже существующего пользователя')
    def test_create_same_user(self):
        response = requests.post(urls.CREATE_USER, data=data.payload_user)
        same_user = response

        assert same_user.status_code == 403 and messages.USER_EXISTS

    @allure.description('Получение статус-кода и сообщения об ошибке при создании пользователя без одного обязательного поля')
    def test_requirement_fields(self):
        response = requests.post(urls.CREATE_USER, data=data.payload_without_password)

        assert response.status_code == 403 and messages.PASSWORD_REQUIRED
