class Registration:
    response_200 = '{"ok":true}'
    response_409 = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    response_400 = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'


class Login:
    response_400 = '{"code":400,"message":"Недостаточно данных для входа"}'
    response_404 = '{"code":404,"message":"Учетная запись не найдена"}'