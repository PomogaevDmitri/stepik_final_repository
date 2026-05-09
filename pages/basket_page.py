from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from .base_page import FormatGener
class BasketPage(BasePage):
    TEXT_BASKET_INFO_IN_MAIN = "Ваша корзина пуста"
    URL_LOGIN = 'basket'
    TEXT_BASKET_INFO_IN_BASKET = "Ваша корзина пуста Продолжить покупки"

    def should_be_basket_to_empty_in_main_page(self):
        assert (self.TEXT_BASKET_INFO_IN_MAIN ==
                self.browser.find_element(*LoginPageLocators.BASKET_TO_EMPTY)
                .get_attribute("textContent")), "Basket is not empty"

    def should_be_basket_to_empty_in_basket_page_text(self):
        text_in_basket = (self.browser.find_element(*BasketPageLocators.
                                                   BASKET_TEXT_IN_TO_BASKET).text)
        text_in_basket = FormatGener.normalize_text(text_in_basket)
        assert self.TEXT_BASKET_INFO_IN_BASKET == text_in_basket, "Basket is not empty"

    def should_be_basket_totals(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_TOTALS), \
            "Basket is not empty"