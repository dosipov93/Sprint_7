import allure
import pytest
from helpers import CourierApi
from utils.generators import generate_courier_data
from constant import Key, Error
from utils.data import REQUIRED_FIELDS


class TestCourier:
    
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self,courier_data):
        response = CourierApi.create_courier(
            login=courier_data[Key.LOGIN],
            password=courier_data[Key.PASSWORD],
            first_name=courier_data[Key.FIRST_NAME])
        response_json = response.json()
        assert response.status_code == 201, (
            'Статус-код создания курьера неверный. '
            f'Ожидался: 201, получен: {response.status_code}'
        )
        assert response_json.get(Key.OK) is True, (
            'Флаг успеха "ok" отсутствует в ответе или равен False'
        )

    @allure.title('Проверка на создание дубликата')
    def test_create_duplicate_courier(self, courier):
        response = CourierApi.create_courier(
            login=courier[Key.LOGIN],
            password=courier[Key.PASSWORD],
            first_name=courier[Key.FIRST_NAME])
        response_json = response.json()
        assert response.status_code == 409, (
            'Статус-код при создании дубликата неверный. '
            f'Ожидался: 409, получен: {response.status_code}'
        )
        assert response_json.get(Key.MESSAGE) == Error.DUPLICATE_LOGIN, (
            'Текст ошибки не соответствует ожидаемому. '
            f'Ожидалось: "{Error.DUPLICATE_LOGIN}", получено: "{response_json.get(Key.MESSAGE)}"'
        )

    @allure.title('Проверка на отсутствие обязательных полей')
    @pytest.mark.parametrize('login, password, first_name', REQUIRED_FIELDS)
    def test_create_courier_without_required_fields(self, login, password, first_name):
        response = CourierApi.create_courier(login=login, password=password, first_name=first_name)
        response_json = response.json()
        assert response.status_code == 400, (
            'Статус-код при отсутствии полей неверный. '
            f'Ожидался: 400, получен: {response.status_code}'
        )
        assert response_json.get(Key.MESSAGE) == Error.MISSING_REQUIRED_FIELDS, (
            'Текст ошибки не соответствует ожидаемому. '
            f'Ожидалось: "{Error.MISSING_REQUIRED_FIELDS}", получено: "{response_json.get(Key.MESSAGE)}"'
        )


        