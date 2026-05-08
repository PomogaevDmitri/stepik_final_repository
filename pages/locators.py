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
    PRICE_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    DOP_URL = f"catalogue/coders-at-work_207/?"
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")