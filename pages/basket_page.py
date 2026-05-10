from config.urls import Urls
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from utils.formatting import Formatting
from config.text_in_page import TextPage

class BasketPage(BasePage):
    def should_be_basket_to_empty_in_main_page(self):
        assert (TextPage.TEXT_BASKET_INFO_IN_MAIN ==
                self.get_attribute_text_in_element(*LoginPageLocators.BASKET_TO_EMPTY)),\
            "Basket is not empty"

    def should_be_basket_to_empty_in_basket_page_text(self):
        text_in_basket = (self.text_in_element(*BasketPageLocators.BASKET_TEXT_IN_TO_BASKET))
        text_in_basket = Formatting.normalize_text(text_in_basket)
        assert TextPage.TEXT_BASKET_INFO_IN_BASKET == text_in_basket, "Basket is not empty"

    def should_be_basket_totals(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_TOTALS), \
            "Basket is not empty"

    def go_to_basket_page(self):
        self.click_element(*BasketPageLocators.BUTTON_TO_BASKET_IN_MAIN)
        assert self.is_url_contains_str(Urls.URL_LOGIN_BASKET), \
            "The URL does not contain the string basket"