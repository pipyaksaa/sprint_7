import requests
import json
from urls import order_url, order_with_filters_url

def create_order_with_specific_color(first_color=None, second_color=None):
    color = [first_color, second_color] if first_color and second_color else [first_color] if first_color else [second_color] if second_color else []

    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": "5",
        "deliveryDate": "2020-06-06",
        "comment": "Sasuke, come back to Konoha",
        "color": color
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(order_url, json=payload, headers=headers)

    return json.loads(response.content)['track'] if response.status_code == 201 else response.text

def get_one_order_from_list_with_first_metro_station():
    response = requests.get(order_with_filters_url)

    return json.loads(response.content)['orders'] if response.status_code == 200 else response.text
