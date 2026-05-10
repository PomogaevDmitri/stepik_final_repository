import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from utils.generation import Generation
from config.urls import Urls

@pytest.mark.need_review
@pytest.mark.catalog
@pytest.mark.parametrize('promo', ["promo=offer0",
                                  "promo=offer1",
                                  "promo=offer2",
                                  "promo=offer3",
                                  "promo=offer4",
                                  "promo=offer5",
                                  "promo=offer6",
                                   pytest.param("promo=offer7",
                                                marks=pytest.mark.xfail
                                                (reason="Здесь бага")),
                                  "promo=offer8",
                                  "promo=offer9"])
def test_guest_can_add_product_to_basket(browser,base_url,promo):
    page = ProductPage(browser, base_url + Urls.DOP_URL_PROMO + promo) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() #Открываем страницу в браузере
    page.should_not_be_success_message() # Проверка, что сообщения нет об успешном добавлении товара в корзину
    page.add_item_to_cart() # Добавление товара в корзину
    page.solve_quiz_and_get_code() # Расчет значения для всплывающего окна
    page.cart_value_after_adding_an_item() # Проверка стоймости корзины
    page.matching_product_name_and_message() # Проверка отображения сообщения после добавления товара

def test_guest_should_see_login_link_on_product_page(browser,base_url):
    page = LoginPage(browser, base_url + Urls.DOP_URL_THE_CITY)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()#Открываем страницу в браузере
    page.should_be_login_link() # Проверка возможности перехода к странице Login

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser,base_url):
    page = ProductPage(browser, base_url + Urls.DOP_URL_THE_CITY)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()#Открываем страницу в браузере
    page.go_to_login_page() # Переход на страницу Login

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser,base_url):
    product = ProductPage(browser, base_url + Urls.DOP_URL_THE_CITY)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product.open()# Открываем страницу в браузере
    basket = BasketPage(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    basket.go_to_basket_page()  # Переход на страницу Basket
    basket.should_be_basket_totals() # Проверка на стоймость корзины
    basket.should_be_basket_to_empty_in_basket_page_text() # Проверка на сообщение в корзине

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser,base_url):
        self.login_page = LoginPage(browser, base_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.login_page.open()#Открываем страницу в браузере
        self.login_page.go_to_login_page() # Переход на страницу Login
        self.login_page.register_new_user(Generation.random_email(),Generation.random_password()) # Регистрация нового пользователя

    def test_user_cant_see_success_message(self, browser,base_url):
        page = ProductPage(browser, base_url + Urls.DOP_URL_THE_CITY)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() #Открываем страницу в браузере
        page.should_not_be_success_message() # Проверка, что сообщения нет об успешном добавлении товара в корзину

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, base_url, promo="promo=offer0"):
        page = ProductPage(browser, base_url + Urls.DOP_URL_PROMO + promo)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # Открываем страницу в браузере
        page.should_not_be_success_message()# Проверка, что сообщения нет об успешном добавлении товара в корзину
        page.add_item_to_cart() # Добавление товара в корзину
        page.solve_quiz_and_get_code() # Расчет значения для всплывающего окна
        page.cart_value_after_adding_an_item() # Проверка стоймости корзины
        page.matching_product_name_and_message() # Проверка отображения сообщения после добавления товара