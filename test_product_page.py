import time

import pytest
from .pages.product_page import ProductPage
from .pages.locators import CataloguePageLocators

@pytest.mark.catalog
def test_guest_can_add_product_to_basket(browser,base_url):

    page = ProductPage(browser, base_url + CataloguePageLocators.DOP_URL)
    page.open() #Открываем страницу в браузере
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.cart_value_after_adding_an_item()
    page.matching_product_name_and_message()
    #time.sleep(900)
