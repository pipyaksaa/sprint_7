import pytest
import allure
from methods.registration import generate_random_string, register_new_courier_with_specific_data
from methods.login import *
from data import Login


class TestLogin:
    @allure.title("Test successful login")
    def test_successful_login(self):
        login = generate_random_string(7)
        password = generate_random_string(6)
        register_new_courier_with_specific_data(login, password)
        assert isinstance(login_user(login, password), int)

    @pytest.mark.parametrize(
        'login, password',
        [
            [generate_random_string(7), ''],
            ['', generate_random_string(7)]
        ]
    )
    @allure.title("Test login without required attribute")
    def test_login_without_required_attribute(self, login, password):
        assert login_user(
            login, password) == Login.response_400

    @allure.title("Test login with typo in login")
    def test_login_with_typo_in_login(self):
        login = generate_random_string(10)
        password = generate_random_string(11)
        register_new_courier_with_specific_data(login, password)
        assert login_user(login[:-1], password) == Login.response_404

    @allure.title("Test login with typo in password")
    def test_login_with_typo_in_password(self):
        login = generate_random_string(10)
        password = generate_random_string(11)
        register_new_courier_with_specific_data(login, password)
        assert login_user(login, password[:-1]) == Login.response_404