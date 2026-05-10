from faker import Faker
class Generation:
    fake = Faker()

    @staticmethod
    # Генерация email
    def random_email():
        return Generation.fake.email()

    @staticmethod
    # Генерация пароля
    def random_password():
        return Generation.fake.password()