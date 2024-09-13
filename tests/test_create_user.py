import requests
import pytest
import allure
from helpers import fake_user_and_order, messages
from helpers.user import User




@allure.title('Проверка создания пользователя')
class TestCreateUser:
    @allure.description('Получение статус-кода 200 при создании курьера')
    def test_create_new_user(self):
        user_data = fake_user_and_order.fake_user_data()
        response = User.create_new_user(user_data)
        access_token = response.json().get('accessToken')

        assert response.status_code == 200

    @allure.description('Получение статус-кода и сообщения об ошибке при попытке создать уже существующего пользователя')
    def test_create_same_user(self, create_delete_user):
        user_data = create_delete_user
        response = User.create_new_user(user_data)

        assert response.status_code == 403 and messages.USER_EXISTS

    @allure.description('Получение статус-кода и сообщения об ошибке при создании пользователя без обязательных полей')
    @pytest.mark.parametrize('user_data', [
        (fake_user_and_order.fake_user_data(include_first_name=False)),
        (fake_user_and_order.fake_user_data(include_email=False)),
        (fake_user_and_order.fake_user_data(include_password=False)),
    ])
    def test_requirement_fields(self, user_data):
        response = User.create_new_user(user_data)

        assert response.status_code == 403 and messages.PASSWORD_REQUIRED
