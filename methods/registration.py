import random
import string
import requests
from urls import reg_url

class CourierRegistration:
    def __init__(self, login=None, password=None, first_name=None):
        self.login = login or self.generate_random_string(10)
        self.password = password or self.generate_random_string(10)
        self.first_name = first_name or self.generate_random_string(10)

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def register_courier(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }
        response = requests.post(reg_url, data=payload)
        return response.text

    def get_credentials(self):
        return self.login, self.password

    @staticmethod
    def register_using_same_credentials():
        courier1 = CourierRegistration()
        courier1.register_courier()

        courier2 = CourierRegistration()
        response = courier2.register_courier()

        return response

    @staticmethod
    def register_without_required_attribute(attribute=None):
        str_value = CourierRegistration().generate_random_string(10)
        first_name = CourierRegistration().generate_random_string(10)

        payload = {
            "login": str_value if attribute != 'login' else None,
            "password": str_value if attribute != 'password' else None,
            "firstName": first_name
        }

        response = requests.post(reg_url, data=payload)
        return response.text

    @staticmethod
    def register_new_courier_with_specific_data(login=None, password=None, first_name=None):
        courier = CourierRegistration(login, password, first_name)
        return courier.register_courier()
