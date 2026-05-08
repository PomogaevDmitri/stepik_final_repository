import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser,base_url):
    page = MainPage(browser, base_url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()       # выполняем метод страницы — переходим на страницу логина
@pytest.mark.skip
def test_guest_should_see_login_link(browser,base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_to_login_form(browser,base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser,base_url):
    page = BasketPage(browser, base_url)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_totals()
    page.should_be_basket_to_empty_in_basket_page_text()
