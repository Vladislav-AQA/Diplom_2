from faker import Faker
from helpers.ingredients import data_ingredients
import random

fake = Faker(locale="ru_RU")


def fake_first_name():
    first_name = fake.first_name()
    return first_name


def fake_email():
    email = fake.email()
    return email

def fake_password():
    password = fake.password()
    return password


def fake_user_data(include_first_name=True, include_email=True, include_password=True):
    user_data = {}
    if include_first_name:
        user_data['name'] = fake_first_name()
    if include_email:
        user_data['email'] = fake_email()
    if include_password:
        user_data['password'] = fake_password()

    return user_data


def fake_order_body():
    buns = [item for item in data_ingredients if item['type'] == 'bun']
    others = [item for item in data_ingredients if item['type'] != 'bun']

    bun = random.choice(buns)

    other_count = random.randint(1, 13)
    selected_others = random.sample(others, other_count)

    selected_ingredients = [bun['_id']] + [item['_id'] for item in selected_others]

    body_order = {"ingredients": selected_ingredients}

    return body_order