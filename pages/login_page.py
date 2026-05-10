from .base_page import BasePage
from .locators import LoginPageLocators
from utils.formatting import Formatting
from config.text_in_page import TextPage
from config.urls import Urls

class LoginPage(BasePage):
    # Обших метод
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    # Проверка Urls
    def should_be_login_url(self):
        assert self.is_url_contains_str(Urls.URL_LOGIN), \
            "The URL does not contain the string login"

    # Проверка отображения формы авторизации
    def should_be_login_form(self):
        assert self.is_element_visibility(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    # Проверка отображения формы регистрации
    def should_be_register_form(self):
        assert self.is_element_visibility(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    # Проверка отображения кнопки для перехода на страницу Login
    def should_be_login_link(self):
        assert self.is_element_visibility(*LoginPageLocators.LOGIN_LINK),\
            "Login link is not presented"

    # Проверка успешной авторизации пользователем
    def should_be_authorized_user(self):
        assert self.is_element_visibility(*LoginPageLocators.USER_ICON),\
            "User icon is not presented,"

    # Регистрация нового пользователя
    def register_new_user(self, email, password):
       self.is_element_send_keys(*LoginPageLocators.REGISTER_EMAIL_FIELD,email)
       self.is_element_send_keys(*LoginPageLocators.
                                 REGISTER_PASSWORD_FIELD, password)
       self.is_element_send_keys(*LoginPageLocators.
                                 REGISTER_COMFORM_PASSWORD_FIELD, password)
       self.click_element(*LoginPageLocators.REGISTER_BUTTON)
       self.is_element_visibility(*LoginPageLocators.
                                 REGISTER_SUCCESSFULLY_TEXT)
       text_in_page = (Formatting.normalize_text
                       (self.get_attribute_text_in_element
                        (*LoginPageLocators.REGISTER_SUCCESSFULLY_TEXT)))

       assert(TextPage.TEXT_REGISTER_SUCCESSFULLY_TEXT == text_in_page), \
           "Registration is not successfully"
       self.should_be_authorized_user()