from faker import Faker

fake_en = Faker('en_US')
fake_ru = Faker('ru_RU')


def generate_courier_data():
    return {
        'login': fake_en.user_name(),
        'password': fake_en.password(),
        'firstName': fake_ru.first_name()
    }