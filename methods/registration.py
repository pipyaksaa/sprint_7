import requests
import random
import string
from urls import reg_url


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(reg_url, data=payload)
    return response.text

def register_using_same_credentials():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    requests.post(reg_url, data=payload)
    response = requests.post(reg_url, data=payload)
    return response.text

def register_new_courier_without_required_attribute(attribute=None):
    generated_string = generate_random_string(10)
    first_name = generate_random_string(10)

    if attribute == 'login':
        payload = {
            "password": generated_string,
            "firstName": first_name
        }
    else:
        payload = {
            "login": generated_string,
            "firstName": first_name
        }

    response = requests.post(reg_url, data=payload)
    return response.text


def register_new_courier_with_specific_data(login=None, password=None, first_name=None):
    login = login or generate_random_string(10)
    password = password or generate_random_string(10)
    first_name = first_name or generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(reg_url, data=payload)
    return response.text