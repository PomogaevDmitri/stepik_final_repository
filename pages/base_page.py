from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    URL_LOGIN_BASKET = 'basket'
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, type_locators, selector):
        try:
            self.browser.find_element(type_locators, selector)
        except NoSuchElementException:
            return False
        return True

    def is_url_contains_str(self, str_in_url):
        try:
            str_in_url in self.browser.current_url
        except NoSuchElementException:
            return False
        return True
    #элемент не появился за указанное время и не должен
    def is_not_element_present(self, type_locators, selector, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout).
             until(EC.presence_of_element_located((type_locators, selector))))
        except TimeoutException:
            return True
        return False

    # элемент не появился за указанное время а должен
    def is_element_presents(self, type_locators, selector, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout).
            until(EC.presence_of_element_located((type_locators, selector))))
            return True
        except TimeoutException:
            return False

    def is_disappeared(self, type_locators, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((type_locators, selector)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BUTTON_TO_BASKET_IN_MAIN).click()
        assert self.is_url_contains_str(self.URL_LOGIN_BASKET), \
            "The URL does not contain the string basket"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \

    def is_element_send_keys(self, type_locators, selector, value):
        try:
            element = self.browser.find_element(type_locators, selector)
            element.clear()
            element.send_keys(value)
            return True
        except NoSuchElementException:
            return False

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