import allure
import pytest
from methods.order import create_order_with_specific_color, get_one_order_from_list_with_first_metro_station


class TestOrder:
    @pytest.mark.parametrize(
        'first_color, second_color',
        [
            ('BLACK', 'GREY'),
            ('BLACK', None),
            (None, 'GREY'),
            (None, None)
        ]
    )
    @allure.title("Test create order with specific color")
    def test_create_order_with_specific_color(self, first_color, second_color):
        assert isinstance(create_order_with_specific_color(first_color, second_color), int)

    @allure.title("Test get order with filters")
    def test_get_order_with_filters(self):
        orders = get_one_order_from_list_with_first_metro_station()
        assert orders and isinstance(orders[0]['id'], int)
