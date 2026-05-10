from faker import Faker
class FormatGener:
    fake = Faker()

    @staticmethod
    #Генерация email
    def random_email():
        return FormatGener.fake.email()

    @staticmethod
    # Генерация пароля
    def random_password():
        return FormatGener.fake.password()

    @staticmethod
    def delete_spaces_in_text(stroke):
            return ''.join(stroke.split())

    @staticmethod
    def normalize_text(text):
        return text.strip()