from faker import Faker


fake = Faker(locale="ru_RU")

email = fake.email()
password = fake.password()
name = fake.name()

payload = {'email': email,
           'password': password,
           'name': name
}

payload_without_password = {
    'email': email,
    'name': name
}

payload_user = {'email': 'test12345@yandex.ru',
           'password': 12345678,
           'name': 'Test-X'

}

ingredients = {
"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
}


class Data:
    NEW_NAME_USER = 'Test12345'
    NEW_PASSWORD_USER = 'qwerty'
    NEW_EMAIL_USER = 'qwerty123@yandex.ru'


