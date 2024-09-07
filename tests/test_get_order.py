import requests
import pytest
import allure
from helpers import urls
from helpers import data
from helpers.create_order import Order

@allure.title('Проверка получения заказа')
class TestGetOrder:

    @allure.description('Получение статус-кода при получении заказа авторизованного пользователя')
    def test_get_order_with_auth(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = requests.post(urls.LOGIN_USER, response.json().get('accessToken'))
        body_order = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}
        Order.create_order(access_token, body_order)
        response_get_order = Order.get_order(access_token)

        assert response_get_order == 200

    @allure.description('Получение статус-кода при получении заказа без авторизации')
    def test_get_order_without_auth(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = None
        body_order = {"ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]}
        Order.create_order(access_token, body_order)
        response_get_order = Order.get_order(access_token)

        assert response_get_order == 401

