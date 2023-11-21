import pytest
from Tests.test_registration import generate_random_string, register_new_courier_with_specific_data
from data import Login
from methods.login import *


class TestLogin:
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
    def test_login_without_required_attribute(self, login, password):
        assert login_user(
            login, password) == Login.response_400

    def test_login_with_typo_in_login(self):
        login = generate_random_string(10)
        password = generate_random_string(11)
        register_new_courier_with_specific_data(login, password)
        assert login_user(login[:-1], password) == Login.response_404

    def test_login_with_typo_in_password(self):
        login = generate_random_string(10)
        password = generate_random_string(11)
        register_new_courier_with_specific_data(login, password)
        assert login_user(login, password[:-1]) == Login.response_404