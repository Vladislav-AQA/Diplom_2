import requests
import pytest
import allure
from helpers import urls
from helpers import data
from helpers.create_order import Order

@allure.title('Проверка создания заказа')
class TestCreateOrder:

    @allure.description('Получение статус-кода при создании заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = requests.post(urls.LOGIN_USER, response.json().get('accessToken'))
        body_order = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}
        response_order = Order.create_order(access_token, body_order)

        assert response_order.status_code == 200

    @allure.description('Получение статус-кода при создании заказа без авторизации')
    def test_create_order_without_auth(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = None
        body_order = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}
        response_order = Order.create_order(access_token, body_order)

        assert response_order.status_code == 200

    @allure.description('Получение статус-кода при создании заказа с авторизацией без ингредиентов')
    def test_create_order_without_ingredients(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = requests.post(urls.LOGIN_USER, response.json().get('accessToken'))
        body_order = {}
        response_order = Order.create_order(access_token, body_order)

        assert response_order.status_code == 400

    @allure.description('Получение статус-кода при создании заказа с неверным хешем ингредиентов')
    def test_invalid_hash_ingredients(self):
        response = requests.post(urls.CREATE_USER, data=data.payload)
        access_token = requests.post(urls.LOGIN_USER, response.json().get('accessToken'))
        body_order = {"ingredients": ["60d3b41abdacab33c6","609646e4e00276b2870"]}
        response_order = Order.create_order(access_token, body_order)

        assert response_order == 500



