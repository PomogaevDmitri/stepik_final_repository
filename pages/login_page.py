
from .base_page import BasePage
from .locators import LoginPageLocators
from utils.formatting import Formatting

class LoginPage(BasePage):
    TEXT_REGISTER_SUCCESSFULLY_TEXT = "Спасибо за регистрацию!"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_contains_str(LoginPageLocators.URL_LOGIN), \
            "The URL does not contain the string login"

    def should_be_login_form(self):
        assert self.is_element_presents(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_presents(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
       self.is_element_send_keys(*LoginPageLocators.REGISTER_EMAIL_FIELD,email)
       self.is_element_send_keys(*LoginPageLocators.
                                 REGISTER_PASSWORD_FIELD, password)
       self.is_element_send_keys(*LoginPageLocators.
                                 REGISTER_COMFORM_PASSWORD_FIELD, password)
       self.click_element(*LoginPageLocators.REGISTER_BUTTON)
       self.is_element_presents(*LoginPageLocators.
                                 REGISTER_SUCCESSFULLY_TEXT)
       text_in_page = (Formatting.normalize_text
                       (self.get_attribute_text_in_element
                        (*LoginPageLocators.REGISTER_SUCCESSFULLY_TEXT)))

       assert(self.TEXT_REGISTER_SUCCESSFULLY_TEXT == text_in_page), "Registration is not successfully"
       self.should_be_authorized_user()