from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    URL_LOGIN = 'login'

class CataloguePageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".btn-cart")
    DOP_URL = f"catalogue/the-shellcoders-handbook_209/?promo=newYear"
