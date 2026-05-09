import pytest
from .pages.product_page import ProductPage
from .pages.locators import CataloguePageLocators

@pytest.mark.catalog
@pytest.mark.parametrize('promo', ["promo=offer0",
                                  "promo=offer1"])
@pytest.mark.xfail(reason="Тут будет падать")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,base_url,promo):
    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_PROMO + promo)
    page.open() #Открываем страницу в браузере
    page.add_item_to_cart()
    page.should_not_be_success_message()

@pytest.mark.catalog
@pytest.mark.parametrize('promo', ["promo=offer0",
                                       "promo=offer1"])
def test_guest_cant_see_success_message(browser,base_url,promo):
    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_PROMO + promo)
    page.open() #Открываем страницу в браузере
    page.should_not_be_success_message()

@pytest.mark.catalog
@pytest.mark.parametrize('promo', ["promo=offer0",
                                     "promo=offer1"])
def test_message_disappeared_after_adding_product_to_basket(browser, base_url, promo):
    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL_PROMO + promo)
    page.open()  # Открываем страницу в браузере
    page.add_item_to_cart()
    page.success_message_hidden()