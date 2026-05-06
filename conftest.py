import pytest
from helpers import CourierApi
from utils.generators import generate_courier_data
from constant import Key


@pytest.fixture
def courier():
    data = generate_courier_data()
    CourierApi.create_courier(login=data[Key.LOGIN], password=data[Key.PASSWORD], first_name=data[Key.FIRST_NAME])

    yield data

    courier_id = CourierApi.get_courier_id(data['login'], data['password'])
    if courier_id:
        CourierApi.delete_courier(courier_id)