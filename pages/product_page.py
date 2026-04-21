from .base_page import BasePage
from .locators import CataloguePageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*CataloguePageLocators.BUTTON_ADD_TO_CART).click()

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
        self.is_element_present(*CataloguePageLocators.PRICE_PRODUCT)
        price_product = self.browser.find_element(*CataloguePageLocators.PRICE_PRODUCT).text
        self.is_element_present(*CataloguePageLocators.PRICE_BASKET)
        price_basket = self.browser.find_element(*CataloguePageLocators.PRICE_BASKET).get_attribute("textContent")
        price_product = self.removing_spaces(price_product)
        price_basket= self.removing_spaces(price_basket)
        assert price_product in price_basket , "The cost of the product and the basket are not equa"

    def matching_product_name_and_message(self):
        assert self.is_element_present(*CataloguePageLocators.NAME_PRODUCT),\
            "Name product is not presented"
        name_product = self.browser.find_element(*CataloguePageLocators.NAME_PRODUCT).text
        assert self.is_element_present(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE),\
            "Name product in message is not presented"
        name_product_in_message = self.browser.find_element(*CataloguePageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert name_product in name_product_in_message, "The product name is not specified in the message."