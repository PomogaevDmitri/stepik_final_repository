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
        price_product = self.browser.find_element(*CataloguePageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*CataloguePageLocators.PRICE_BASKET).get_attribute("textContent")
        price_product = ''.join(price_product.split())
        price_basket = ''.join(price_basket.split())
        assert price_product in price_basket