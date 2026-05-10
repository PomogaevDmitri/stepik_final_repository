from .base_page import BasePage
from utils.formatting import Formatting
from .locators import CataloguePageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.click_element(*CataloguePageLocators.BUTTON_ADD_TO_CART)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def cart_value_after_adding_an_item(self):
        assert self.is_element_visibility(*CataloguePageLocators.PRICE_PRODUCT),\
            f"Элемента {CataloguePageLocators.PRICE_PRODUCT} нет"
        price_product = self.text_in_element(*CataloguePageLocators.PRICE_PRODUCT)
        assert self.is_element_visibility(*CataloguePageLocators.PRICE_BASKET),\
            f"Элемента {CataloguePageLocators.PRICE_BASKET} нет"
        price_basket = self.get_attribute_text_in_element(*CataloguePageLocators.PRICE_BASKET)
        price_product = Formatting.delete_spaces_in_text(price_product)
        price_basket = Formatting.delete_spaces_in_text(price_basket)
        assert price_product == price_basket , "The cost of the product and the basket are not equa"

    def matching_product_name_and_message(self):
        assert self.is_element_visibility(*CataloguePageLocators.NAME_PRODUCT),\
            "Name product is not presented"
        name_product = self.text_in_element(*CataloguePageLocators.NAME_PRODUCT)
        assert self.is_element_visibility(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE),\
            "Name product in message is not presented"
        name_product_in_message = self.text_in_element(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE)
        assert name_product == name_product_in_message, "The product name is not specified in the message."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_hidden(self):
        assert self.is_disappeared(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE), \
            "The success message was not hidden"