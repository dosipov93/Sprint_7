import allure
import pytest
from helpers import OrderApi


class TestOrderList:

    @allure.title('Получение списка заказов')
    def test_get_order_list(self):
        response = OrderApi.get_orders()
        response_json = response.json()
        assert response.status_code == 200, (
            'Статус-код запроса списка заказов неверный. '
            f'Ожидался: 200, получен: {response.status_code}'
        )
        assert isinstance(response_json, dict) and 'orders' in response_json, (
            'Ответ должен быть объектом с полем "orders". '
            f'Получено: {type(response_json).__name__}'
        )
        assert isinstance(response_json['orders'], list), (
            'Поле "orders" должно содержать список заказов. '
            f'Получен тип: {type(response_json["orders"]).__name__}'
        )


        