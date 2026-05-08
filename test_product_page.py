import time

import pytest
from .pages.product_page import ProductPage
from .pages.locators import CataloguePageLocators

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

    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL + promo)
    page.open() #Открываем страницу в браузере
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.cart_value_after_adding_an_item()
    page.matching_product_name_and_message()

