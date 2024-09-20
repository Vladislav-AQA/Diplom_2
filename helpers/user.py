import requests
from helpers import urls


class User:

    @staticmethod
    def create_new_user(user_data):
        response = requests.post(urls.CREATE_USER, json=user_data)
        return response

    @staticmethod
    def delete_user(access_token):
        headers_delete = {
            'Accept': 'application/json',
            'Authorization': f'{access_token}'
        }

        response_delete = requests.delete(urls.DELETE_USER, headers=headers_delete)
        return response_delete

    @staticmethod
    def log_in(login, password):
        response_login = requests.post(urls.LOGIN_USER, json={'email': login, 'password': password})
        return response_login

    @staticmethod
    def edit_data_user(access_token, update_user):
        headers_edit = {
            'Accept': 'application/json',
            'Authorization': f'{access_token}'
        }
        
        response_edit = requests.patch(urls.CHANGE_USER_DATA, headers=headers_edit, json=update_user)
        return response_edit

