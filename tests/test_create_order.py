import allure
from helpers.order import Order
from helpers.user import User
from helpers.problem_ingredients import problem_ingredients
from helpers.fake_user_and_order import fake_order_body


@allure.title('Проверка создания заказа')
class TestCreateOrder:

    @allure.description('Получение статус-кода при создании заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth(self, login_user):
        access_token = login_user.json().get('accessToken')
        order_body = fake_order_body()
        response_order = Order.create_order(access_token, order_body)

        assert response_order.status_code == 200

    @allure.description('Получение статус-кода при создании заказа без авторизации')
    def test_create_order_without_auth(self, create_delete_user):
        user_data = create_delete_user
        email = user_data.get('email', '')
        password = user_data.get('password', '')
        User.log_in(user_data.get('email', email), user_data.get('password', password))
        access_token = None
        order_body = fake_order_body()
        response_order = Order.create_order(access_token, order_body)

        assert response_order.status_code == 200

    @allure.description('Получение статус-кода при создании заказа с авторизацией без ингредиентов')
    def test_create_order_without_ingredients(self, login_user):
        access_token = login_user.json().get('accessToken')
        order_body = None
        response_order = Order.create_order(access_token, order_body)

        assert response_order.status_code == 400

    @allure.description('Получение статус-кода при создании заказа с неверным хешем ингредиентов')
    def test_invalid_hash_ingredients(self, login_user):
        access_token = login_user.json().get('accessToken')
        order_body = problem_ingredients
        response_order = Order.create_order(access_token, order_body)

        assert response_order.status_code == 400



