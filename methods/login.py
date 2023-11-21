
import requests
import json
from urls import login_url


def login_user(login='', password=''):

    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(login_url, data=payload)

    if response.status_code == 200:
        return json.loads(response.content)['id']
    else:
        return response.text