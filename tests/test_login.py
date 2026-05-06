import allure
import pytest
from helpers import CourierApi
from utils.data import INVALID_COURIER_DATA as INVALID, LOGIN_REQUIRED_FIELDS as FIELD
from utils.generators import generate_courier_data
from constant import Key, Error


class TestLogin:

    @allure.title('Успешный вход курьера')
    def test_login_success(self, courier):
        response = CourierApi.login_courier(login=courier[Key.LOGIN], password=courier[Key.PASSWORD])
        response_json = response.json()
        assert response.status_code == 200, (
            'Статус-код авторизации неверный '
            f'Ожидался: 200, получен: {response.status_code}'
        )
        assert response_json.get(Key.ID) > 0, (
            'Поле "id" отсутствует или некорректно. '
            f'Получено: "{response_json.get(Key.ID)}"'
        )

    @allure.title('Попытка авторизация с неверным паролем')
    def test_login_wrong_password(self, courier):
        response = CourierApi.login_courier(login=courier[Key.LOGIN], password=INVALID['password'])
        response_json = response.json()
        assert response.status_code == 404, (
            'Статус-код попытки авторизации с неверным паролем, неверный. '
            f'Ожидался: 404, получен: {response.status_code}'
        )
        assert response_json.get(Key.MESSAGE) == Error.ACCOUNT_NOT_FOUND, (
            'Текст ошибки не соответствует ожидаемому '
            f'Ожидалось: "{Error.ACCOUNT_NOT_FOUND}", получено: "{response_json.get(Key.MESSAGE)}"'
        )
    @allure.title('Попытка авторизации с несуществующими данными')
    def test_login_nonexistent_user(self):
        response = CourierApi.login_courier(login=INVALID['login'], password=INVALID['password'])
        response_json = response.json()
        assert response.status_code == 404, (
            'Статус-код при входе с несуществующим логином неверный. '
            f'Ожидался: 404, получен: {response.status_code}'
        )
        assert response_json.get(Key.MESSAGE) == Error.ACCOUNT_NOT_FOUND, (
            'Текст ошибки не соответствует ожидаемому. '
            f'Ожидалось: "{Error.ACCOUNT_NOT_FOUND}", получено: "{response_json.get(Key.MESSAGE)}"'
        )

    @allure.title('Попытка авторизации с отсутствием обязательных полей')
    @pytest.mark.parametrize('login, password', FIELD)
    def test_login_missing_fields(self, login, password):
        response = CourierApi.login_courier(login=login, password=password)
        response_json = response.json()
        assert response.status_code == 400, (
            'Статус-код при отсутствии обязательных полей неверный. '
            f'Ожидался: 400, получен: {response.status_code}'
        )
        assert response_json.get(Key.MESSAGE) == Error.MISSING_LOGIN_CREDENTIALS, (
            'Текст ошибки не соответствует ожидаемому. '
            f'Ожидалось: "{Error.MISSING_LOGIN_CREDENTIALS}", получено: "{response_json.get(Key.MESSAGE)}"'
        )



        