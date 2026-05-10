import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import CataloguePageLocators
from .pages.basket_page import FormatGener

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
                                                (reason="Бага найденная")),
                                  "promo=offer8",
                                  "promo=offer9"])
def test_guest_can_add_product_to_basket(browser,base_url,promo):

    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_PROMO + promo)
    page.open() #Открываем страницу в браузере
    page.should_not_be_success_message()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.cart_value_after_adding_an_item()
    page.matching_product_name_and_message()

def test_guest_should_see_login_link_on_product_page(browser,base_url):
    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_THE_CITY)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser,base_url):
    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_THE_CITY)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser,base_url):
    product = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_THE_CITY)
    product.open()
    basket = BasketPage(browser, browser.current_url)
    basket.go_to_basket_page()
    basket.should_be_basket_totals()
    basket.should_be_basket_to_empty_in_basket_page_text()

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser,base_url):
        self.login_page = LoginPage(browser, base_url)
        self.login_page.open()
        self.login_page.go_to_login_page()
        self.login_page.register_new_user(FormatGener.random_email(),FormatGener.random_password())

    def test_user_cant_see_success_message(self, browser,base_url):
        page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_THE_CITY)
        page.open() #Открываем страницу в браузере
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, base_url ):
        page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_THE_CITY)
        page.open()  # Открываем страницу в браузере
        page.should_not_be_success_message()
        page.add_item_to_cart()
        page.cart_value_after_adding_an_item()
        page.matching_product_name_and_message()