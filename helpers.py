import allure
import requests
from constant import Key, API



class CourierApi:

    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(login, password, first_name):
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        response = requests.post(API.COURIER_CREATE, json=payload)
        return response
    
    @staticmethod
    @allure.step('Авторизовать курьера')
    def login_courier(login, password):
        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(API.COURIER_LOGIN, json=payload)
        return response
    
    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(courier_id):
        response = requests.delete(f"{API.COURIER_DELETE}/{courier_id}")
        return response
    
    @staticmethod
    @allure.step('Получить "id" курьера')
    def get_courier_id(login, password):
        response = CourierApi.login_courier(login, password)
        if response.status_code == 200:
            return response.json().get(Key.ID)
        return None
    
class OrderApi:

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(order_data):
        response = requests.post(API.ORDER_CREATE, json=order_data)
        return response
    
    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders():
        response = requests.get(API.ORDER_LIST)
        return response