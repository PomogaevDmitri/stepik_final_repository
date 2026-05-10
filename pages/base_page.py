from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config.urls import Urls
from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Открытие ссылки
    def open(self):
        self.browser.get(self.url)

    # Поиск элемента
    def find_element(self, type_locators, selector):
        return self.browser.find_element(type_locators, selector)

    # Клик по элементу
    def click_element(self, type_locators, selector):
        self.find_element(type_locators, selector).click()

    # Получение значения text из элемента
    def text_in_element(self, type_locators, selector):
        return self.find_element(type_locators, selector).text

    # Получение атрибута textContent из элемента
    def get_attribute_text_in_element(self, type_locators, selector):
        return self.find_element(type_locators, selector).get_attribute("textContent")

    # Очистка поля и заполнение значением
    def is_element_send_keys(self, type_locators, selector, value):
        element = self.find_element(type_locators, selector)
        element.clear()
        element.send_keys(value)

    # Проверка Urls
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
    def is_element_visibility(self, type_locators, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((type_locators, selector)))
            return True
        except TimeoutException:
            return False

    # элемент должен пропасть,иначе ошибка
    def is_disappeared(self, type_locators, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((type_locators, selector)))
        except TimeoutException:
            return False
        return True

    # Переход на страницу логина, в идеале перенести в login_page
    def go_to_login_page(self):
        login_link = self.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_visibility(*BasePageLocators.LOGIN_FORM), "Login form is not presented"

