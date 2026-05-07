import allure
import pytest
from constant import Key
from helpers import OrderApi
from utils.data import ORDERS_DATA


class TestOrders:

    @allure.title("Создание заказа с параметрами")
    @pytest.mark.parametrize('order_data',ORDERS_DATA)
    def test_create_order_with_param(self, order_data):
        response = OrderApi.create_order(order_data)
        response_json = response.json()
        assert response.status_code == 201, (
            'Статус-код создания заказа неверный '
            f'Ожидался: 201, получен: {response.status_code}'
        )
        assert Key.TRACK in response_json, (
            'В ответе отсутствует поле "track"'
        )
        assert response_json.get(Key.TRACK) > 0, (
            'Значение "track" должно быть положительным. '
            f'Получено: "{response_json.get(Key.TRACK)}"'
        )


        