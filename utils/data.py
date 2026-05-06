# utils/data.py

ORDERS_DATA = [
    {
        "address": "ул. Ленина, 10",
        "metroStation": 1,
        "phone": "+79991112233",
        "rentTime": 1,
        "deliveryDate": "2026-05-10",
        "comment": "Тест с одним цветом",
        "color": ["BLACK"]
    },
    {
        "address": "пр. Мира, 5",
        "metroStation": 2,
        "phone": "+79992223344",
        "rentTime": 2,
        "deliveryDate": "2026-05-11",
        "comment": "Тест с другим цветом",
        "color": ["GREY"]
    },
    {
        "address": "ул. Победы, 15",
        "metroStation": 3,
        "phone": "+79993334455",
        "rentTime": 3,
        "deliveryDate": "2026-05-12",
        "comment": "Тест с двумя цветами",
        "color": ["BLACK", "GREY"]
    },
    {
        "address": "ш. Энтузиастов, 20",
        "metroStation": 4,
        "phone": "+79994445566",
        "rentTime": 4,
        "deliveryDate": "2026-05-13",
        "comment": "Тест без цвета",
        "color": []
    }
]

REQUIRED_FIELDS = [
    (None, 'any_password', 'Test'),
    ('any_login', None, None),
    (None, None, 'Test')
]

LOGIN_REQUIRED_FIELDS = [
    ('any_login', ''),
    ('', 'any_password'),
    ('', '')
]

INVALID_COURIER_DATA = {'login': 'invalid_login', 'password': 'invalid_password'}