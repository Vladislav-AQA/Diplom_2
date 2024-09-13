import requests
import pytest
import allure
from helpers import urls
from helpers.order import Order
from helpers.user import User
from helpers.fake_user_and_order import fake_order_body

@allure.title('Проверка получения заказа')
class TestGetOrder:

    @allure.description('Получение статус-кода при получении заказа авторизованного пользователя')
    def test_get_order_with_auth(self, login_user):
        access_token = login_user.json().get('accessToken')
        order_body = fake_order_body()
        Order.create_order(access_token, order_body)
        response_get_order = Order.get_order(access_token)

        assert response_get_order.status_code == 200

    @allure.description('Получение статус-кода при получении заказа без авторизации')
    def test_get_order_without_auth(self, login_user):
        access_token = login_user.json().get('accessToken')
        order_body = fake_order_body()
        Order.create_order(access_token, order_body)
        access_token = None
        response_get_order = Order.get_order(access_token)

        assert response_get_order.status_code == 401

