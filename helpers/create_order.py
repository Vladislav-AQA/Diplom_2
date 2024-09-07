import requests
from helpers import urls
class Order:
    def create_order(self, access_token, body_order):
        order_headers = {
            'Accept': 'application/json',
            'Authorization': access_token
        }
        order_response = requests.post(urls.CREATE_ORDER, headers=order_headers, json={"ingredients": [
            "60d3b41abdacab0026a733c6",
            "609646e4dc916e00276b2870"]})
        return order_response

    def get_order(self, access_token):
        order_headers = {
            'Accept': 'application/json',
            'Authorization': access_token
        }
        get_order_response = requests.get(urls.GET_USER_ORDER, headers=order_headers)
        return get_order_response
