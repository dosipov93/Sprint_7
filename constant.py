# constant.py


class API:
    BASE_URL = 'https://qa-scooter.education-services.ru'
    
    COURIER_CREATE = f'{BASE_URL}/api/v1/courier'
    COURIER_LOGIN = f'{BASE_URL}/api/v1/courier/login'
    COURIER_DELETE = f'{BASE_URL}/api/v1/courier'
    
    ORDER_CREATE = f'{BASE_URL}/api/v1/orders'
    ORDER_LIST = f'{BASE_URL}/api/v1/orders'
    ORDER_TRACK = f'{BASE_URL}/api/v1/orders/track'
    ORDER_ACCEPT = f'{BASE_URL}/api/v1/orders/accept'
    ORDER_FINISH = f'{BASE_URL}/api/v1/orders/finish'
    ORDER_CANCEL = f'{BASE_URL}/api/v1/orders/cancel'
    


class Key:
    OK = "ok"
    ID = "id"
    TRACK = "track"
    ORDERS = "orders"
    ORDER = "order"
    PAGE_INFO = "pageInfo"
    AVAILABLE_STATIONS = "availableStations"
    
    LOGIN = "login"
    PASSWORD = "password"
    FIRST_NAME = "firstName"
    
    COLOR = "color"
    COMMENT = "comment"
    STATUS = "status"
    MESSAGE = 'message'

class Error:
    DUPLICATE_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    MISSING_REQUIRED_FIELDS = 'Недостаточно данных для создания учетной записи'
    
    MISSING_LOGIN_CREDENTIALS = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    
    ORDER_NOT_FOUND = 'Заказ не найден'
    COURIER_NOT_FOUND = 'Курьера с таким id не существует'
    ORDER_IN_PROGRESS = 'Этот заказ уже в работе'
    INVALID_SEARCH_PARAMS = 'Недостаточно данных для поиска'