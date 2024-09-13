import requests
from helpers import urls

class Order:

    @staticmethod
    def create_order(access_token, body_order):
        headers_order = {
            'Accept': 'application/json',
            'Authorization': access_token
        }

        response_order = requests.post(urls.CREATE_ORDER, headers=headers_order, json=body_order)
        return response_order

    @staticmethod
    def get_order(access_token):
        headers_order =  {
            'Accept': 'application/json',
            'Authorization': access_token
        }

        response_get_order = requests.get(urls.GET_USER_ORDER, headers=headers_order)
        return response_get_order